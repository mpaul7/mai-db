import re
import os
import click
import subprocess
import pandas as pd
import yaml
from collections import defaultdict

import mapping_asn_v2

static_ip = defaultdict(list)
ip_not_found = defaultdict(list)

from mapping_asn_v2 import *

@click.command(name='current')
def current_db():
    """Update Current DB"""
    with open('params.yaml', 'r') as f:
        params = yaml.safe_load(f)
    print(params)
    data_source_dir = params['current_db']['data_source_dir']
    os.makedirs(params['current_db']['data_dir'], exist_ok=True)
    file_name = params['current_db']['file_name']
    file_path = os.path.join(data_source_dir, file_name)
    cp = subprocess.run(f"cp {file_path} {params['current_db']['data_dir']}", shell=True)
    cp.check_returncode()   
    
def _run_whois_impl(iterations=1):
    """ Implementation of whois command to retrieve route information """
    def extract_route_info(whois_output):
        """ Extract route information from whois output """
        route_info = []
        pattern = r'route:\s+([\d./]+)'
        matches = re.findall(pattern, whois_output)
        route_info.extend(matches)
        return route_info
    dfs = []
    
    for i in range(iterations):
        try:
            for app, asn_list in mapping_asn_v2.apps_asn.items():
                click.echo(f'\nRetrieving data for app -> [{app}]')
                for asn in asn_list:
                    cmd = "whois -h whois.radb.net -- -i origin asn"
                    whois_cmd = ["whois", "-h", "whois.radb.net", "--", "-i", "origin", asn]
                    process = subprocess.Popen(whois_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    stdout, stderr = process.communicate()
                    stdout = stdout.decode('utf-8')
                    stderr = stderr.decode('utf-8')

                    if stderr:
                        click.echo(f'Error occurred while running whois command for ASN {asn}: {stderr}')
                        continue

                    ips = extract_route_info(stdout)
                    click.echo(f'ASN - [{asn}] -> IPs -[{len(ips)}]')
                    
                    if ips:
                        static_ip[app].extend(set(ips))
                    else:
                        ip_not_found[app].append(asn)
                        
            tuples = [(subnet, k) for k, v in static_ip.items() for subnet in v]
            df = pd.DataFrame.from_records(tuples, columns=['net_address', 'label'])
            df['source'] = 'asn'
            dfs.append(df)
        except Exception as e:
            click.echo(f"An error occurred: {e}")
    df = pd.concat(dfs)
    df.drop_duplicates(subset=['net_address'], keep='first', inplace=True)
    return df, ip_not_found

@click.command(name='asn')
def run_whois():
    """ Run whois command to retrieve route information """
    with open('params.yaml', 'r') as f:
        params = yaml.safe_load(f)
    iterations = params['retrieve_db']['iterations']

    df, ip_not_found = _run_whois_impl(iterations=iterations)
    
    click.echo(f"\n{'='*50}\n")
    click.echo(df.groupby('label').size())
    click.echo(f'\nTotal number of network addresses: {len(df)}')
    click.echo(f'IPs not found: {ip_not_found}')
    click.echo(f"\n{'='*50}\n")
    file_name = params['retrieve_db']['output_file_name']
    output_file = os.path.join(params['retrieve_db']['data_dir'], file_name)
    df.to_csv(output_file, index=False)
    
    non_retrieved_file = os.path.join(params['retrieve_db']['data_dir'], f"non_{file_name}")
    with open(non_retrieved_file, 'w') as f:
        for app, asns in ip_not_found.items():
            f.write(f"{app}: {asns}\n")


@click.command(name='update')
def update_current_db():
    """Update Current DB"""
    with open('params.yaml', 'r') as f:
        params = yaml.safe_load(f)
    
    """Current DB
     - Read current DB
     - Add source column
    """
    current_data_dir = params['current_db']['data_dir']
    current_file_name = params['current_db']['file_name']
    current_file = os.path.join(current_data_dir, current_file_name)
    current_df = pd.read_csv(current_file)
    current_df['source'] = 'unknown'

    """Retrieved DB
     - Retrieve IP addresses from ASN
     - Remove duplicates
    """
    retrieve_data_dir = params['retrieve_db']['data_dir']
    retrieve_file_name = params['retrieve_db']['output_file_name']
    retrieve_file = os.path.join(retrieve_data_dir, retrieve_file_name)
    retrieve_df = pd.read_csv(retrieve_file)
    retrieve_df.drop_duplicates(subset=['net_address'], keep='first', inplace=True)
    
    """Updated DB
     - Merge current and retrieved DB
     - Remove duplicates
    """
    updated_data_dir = params['updated_db']['data_dir']
    os.makedirs(updated_data_dir, exist_ok=True)
    updated_file_name = params['updated_db']['file_name']
    updated_file = os.path.join(updated_data_dir, updated_file_name)
    updated_df = pd.concat([current_df, retrieve_df], ignore_index=True)
    updated_df.drop_duplicates(subset=['net_address'], keep='first', inplace=True)
    updated_df.to_csv(updated_file, index=False)
    
    """Compare record counts by label between current and retrieved DBs
        - Generate comparison report
        - Display comparison report
        - Save comparison report to file in updated_data_dir
        """
    current_by_label = current_df.groupby('label').size()
    retrieved_by_label = retrieve_df.groupby('label').size()
    
    current_by_label = current_df.groupby('label').size().rename("current_IP_count")
    retrieved_by_label = retrieve_df.groupby('label').size().rename("retrieved_IP_count")

    # Merge both series into a single DataFrame for comparison
    comparison_df = pd.concat([current_by_label, retrieved_by_label], axis=1).fillna(0)

    # Convert NaN to 0 and ensure integer type
    comparison_df = comparison_df.astype(int)

    # Calculate the difference
    comparison_df["difference"] = comparison_df["current_IP_count"] - comparison_df["retrieved_IP_count"]
    comparison_df.sort_values(by='difference', ascending=False, inplace=True)
    comparison_df.to_csv(os.path.join(updated_data_dir, f"comparison_current_retrieved_db.csv"))

    # Display the comparison
    click.echo(f"\n{'='*50}\n")
    click.echo(f"Comparison Report\n")
    click.echo(comparison_df)
    click.echo(f"\n{'='*50}\n")

    
@click.command(name='final')
def final_db():
    """Final DB
        - Remove duplicates from updated DB
        - Save to file as final DB
    - Generate DB comparison report
"""
    """Update final DB"""
    with open('params.yaml', 'r') as f:
        params = yaml.safe_load(f)
        
    final_data_dir = params['final_db']['data_dir']
    os.makedirs(final_data_dir, exist_ok=True)
    final_file_name = params['final_db']['file_name']
    final_file = os.path.join(final_data_dir, final_file_name)
    
    updated_data_dir = params['updated_db']['data_dir']
    updated_file_name = params['updated_db']['file_name']
    updated_file = os.path.join(updated_data_dir, updated_file_name)
    updated_df = pd.read_csv(updated_file)
    final_df = updated_df[['net_address', 'label']].copy()
    final_df.to_csv(final_file, index=False)

    # """Compare record counts by label between current and retrieved DBs
    # - Generate comparison report
    # - Display comparison report
    # - Save comparison report to file in updated_data_dir
    # """
    # current_by_label = current_df.groupby('label').size()
    # retrieved_by_label = retrieve_df.groupby('label').size()
    
    # current_by_label = current_df.groupby('label').size().rename("current_IP_count")
    # retrieved_by_label = retrieve_df.groupby('label').size().rename("retrieved_IP_count")

    # # Merge both series into a single DataFrame for comparison
    # comparison_df = pd.concat([current_by_label, retrieved_by_label], axis=1).fillna(0)

    # # Convert NaN to 0 and ensure integer type
    # comparison_df = comparison_df.astype(int)

    # # Calculate the difference
    # comparison_df["difference"] = comparison_df["current_IP_count"] - comparison_df["retrieved_IP_count"]
    # comparison_df.sort_values(by='difference', ascending=False, inplace=True)
    # comparison_df.to_csv(os.path.join(updated_data_dir, f"comparison_current_retrieved_db.csv"))

    # # Display the comparison
    # click.echo(f"\n{'='*50}\n")
    # click.echo(f"Comparison Report\n")
    # click.echo(comparison_df)
    # click.echo(f"\n{'='*50}\n")
    

@click.group()
def entrypoint():
    """ Based on ASN, generate a CSV file containing 'net_address' and 'label' """

entrypoint.add_command(current_db)
entrypoint.add_command(run_whois)
entrypoint.add_command(update_current_db)
entrypoint.add_command(final_db)