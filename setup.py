from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "mai-db"
AUTHOR_USER_NAME = "mpaul7"
SRC_REPO = "mai-db"
AUTHOR_EMAIL = "mpaul7@gmail.com"

setup(
    name="mdb",
    version=__version__,
    author="Manjinder",
    author_email="mpaul7@gmail.com",
    description="DB project",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.8.10 ",
    install_requires=["pandas",
                       "numpy", 
                       "Click==8.1.3", 
                       "setuptools>=56.1.0"
                       ],
    entry_points={
        "console_scripts": [
            "mdb=src.retrieve_ip:entrypoint"
        ]
    }
)   
