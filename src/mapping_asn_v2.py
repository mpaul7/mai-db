
"""
This is a list of applcation covered by nDPI static_ip database. 

"""


STATIC_IP_NDPI = ['ALIBABA', 'AMAZON', 'APPLE', 'AVAST', 'BLOOMBERG', 'CACHEFLY', 'CLOUDFLARE', 'CRAWLER', 'DISCORD', 'DISNEYPLUS',
    'DROPBOX', 'EDGECAST', 'EPICGAMES', 'ETHEREUM', 'FACEBOOK', 'GITHUB', 'GOOGLE', 'GOTO', 'HULU', 'LINE', 'MICROSOFT', 'MS',
    'MULLVAD', 'NETFLIX', 'NVIDIA', 'OPENDNS', 'PROTONVPN', 'RIOTGAMES', 'ROBLOX', 'SKYPE', 'STARCRAFT', 'STEAM', 'SUBSCRIBER',
    'TEAMVIEWER', 'TELEGRAM', 'TENCENT', 'THREEMA', 'TOR', 'TWITCH', 'TWITTER', 'UBUNTUONE', 'VK', 'WEBEX', 'WHATSAPP', 'YANDEX', 'ZOOM']

STATIC_IP_MISSING_NDPI = ['bilibilli', 'dailymotion', 'deezer', 'instagram', 'kakao', 'signal', 'netnease', 'slack', 'snaapchat', 
                     'soundcloud', 'spotify', 'tanga', 'tiktok', 'viber', 'wechat', ]

"""
List of ASNs populated from website
https://bgpview.io/ 
"""

"""
List of 20 apps used in twc_v1.5.4
Data: 10-05-2024
"""

apps_asn = {
    'Adform': ['AS198622'],
    'Adjust': ['AS205184', 'AS396535', 'AS61273'],
    'Akamai': ['AS12222', 'AS133103', 'AS16625', 'AS16702', 'AS17204', 'AS18680', 'AS18717', 'AS20189', 'AS20940', 'AS21342', 'AS21357', 'AS21399', 'AS22207', 'AS22452', 'AS23454', 'AS23455', 'AS23903', 'AS24319', 'AS26008', 'AS30675', 'AS31107', 'AS31108', 'AS31109', 'AS31110', 'AS31377', 'AS33047', 'AS33905', 'AS34164', 'AS34850', 'AS35204', 'AS35993', 'AS35994', 'AS36183', 'AS393560', 'AS39836', 'AS43639', 'AS55409', 'AS55770', 'AS63949'],
    'Alibaba': ['AS59055', 'AS59054', 'AS59053', 'AS59052', 'AS59051', 'AS59028', 'AS45104', 'AS45103', 'AS45102', 'AS37963', 'AS34947', 'AS211914', 'AS134963'],
    'Amazon': ['AS9059', 'AS8987', 'AS801', 'AS7224', 'AS699', 'AS62785', 'AS58588', 'AS40045', 'AS400098', 'AS399991', 'AS399834', 'AS395343', 'AS39111', 'AS38895', 'AS36263', 'AS264167', 'AS21664', 'AS19047', 'AS17493', 'AS16509', 'AS14618', 'AS135630', 'AS10291', 'AS10124', 'AS262486', 'AS262772', 'AS263639', 'AS264344', 'AS264509', 'AS266122', 'AS266194', 'AS267242', 'AS268063', 'AS271017', 'AS271047', 'AS52994', 'AS61577'],
    'Apple': ['AS714', 'AS63707', 'AS6185', 'AS47995', 'AS400506', 'AS396959', 'AS396918', 'AS35026', 'AS31128', 'AS2709', 'AS216183', 'AS198675', 'AS150711', 'AS139901', 'AS138575', 'AS136716', 'AS136581', 'AS11046', 'AS1042', 'AS1036', 'AS135855', 'AS14009', 'AS198926', 'AS206368', 'AS208629', 'AS210443', 'AS23196', 'AS54506'],
    'Asana': ['AS58303', 'AS57457', 'AS398399', 'AS39330', 'AS31549'],
    'Baidu': ['AS133746', 'AS199506', 'AS38365', 'AS38627', 'AS55967', 'AS63288', 'AS63729', 'AS63728', 'AS45085', 'AS45076', 'AS131141', 'AS131140', 'AS131139'],
    'Bbc': ['AS9156', 'AS34158', 'AS31459', 'AS2818'],
    'Bilibili': ['AS63828', 'AS140943', 'AS140633'],
    'Bing': ['AS138832', 'AS199304', 'AS201529', 'AS207842', 'AS208949', 'AS210008', 'AS210010', 'AS214014', 'AS22401', 'AS393559', 'AS4190', 'AS6933'],
    'Citrix': ['AS132361', 'AS43204', 'AS60825', 'AS62795'],
    # 'Dailymotion': ['AS57068', 'AS41690', 'AS393269', 'AS134607'],
    # 'Deepintent': ['AS398989', 'AS399183', 'AS401006'],
    # 'Disney': ['AS8137', 'AS54330', 'AS53578', 'AS46557', 'AS400805', 'AS400558', 'AS400557', 'AS40051', 'AS400265', 'AS399490', 'AS399344', 'AS398849', 'AS396054', 'AS30311', 'AS30224', 'AS29736', 'AS25932', 'AS23344', 'AS22604', 'AS205757', 'AS20374', 'AS17122', 'AS15260', 'AS140693', 'AS13379', 'AS11812', 'AS11251'],
    # 'DNSFilter': ['AS64089'],
    # 'Dropbox': ['AS62190', 'AS54372', 'AS393874', 'AS203719', 'AS200499', 'AS19679'],
    # 'Ebay': ['AS11643', 'AS131796', 'AS14494', 'AS24331', 'AS40533', 'AS43193', 'AS43392', 'AS53358', 'AS6907', 'AS60939', 'AS62955', 'AS9424'],
    # 'Facebook': ['AS63293', 'AS54115', 'AS34825', 'AS32934', 'AS149642'],
    # 'Foxnews': ['AS53294'],
    # 'Ftp': ['AS149811'],
    # 'Github': ['AS36459'],
    # 'Google': ['AS6432', 'AS55023', 'AS45566', 'AS43515', 'AS41264', 'AS40873', 'AS396982', 'AS395973', 'AS394639', 'AS394507', 'AS394089', 'AS36987', 'AS36561', 'AS36520', 'AS36492', 'AS36411', 'AS36385', 'AS36384', 'AS36383', 'AS36040', 'AS36039', 'AS32381', 'AS26910', 'AS26684', 'AS22859', 'AS22577', 'AS19527', 'AS19448', 'AS19425', 'AS16591', 'AS16550', 'AS15169', 'AS13949', 'AS139190', 'AS139070', 'AS200238', 'AS24424', 'AS264324'],
    # 'Goto': ['AS141167', 'AS16815', 'AS20104', 'AS208362', 'AS21866', 'AS39673', 'AS52621', 'AS9465'],
    # 'Gotomeeting': ['AS6643', 'AS395424', 'AS21866', 'AS213380', 'AS20104', 'AS16815', 'AS131943'],
    # 'Hulu': ['AS23286'],
    # 'Kakao': ['AS131858', 'AS38099', 'AS38667', 'AS38678', 'AS45991', 'AS9958', 'AS152199'],
    # 'Kakaotalk': ['AS9764', 'AS7625', 'AS45991', 'AS38678', 'AS38099', 'AS23588', 'AS18160', 'AS152199', 'AS131858', 'AS131828', 'AS10158', 'AS38667', 'AS9958'],
    # 'Line': ['AS7482'],
    # 'Linkedin': ['AS55163', 'AS40793', 'AS20366', 'AS202745', 'AS20049', 'AS14413', 'AS137709', 'AS13443', 'AS132466', 'AS132406', 'AS30427'],
    # 'Meta': ['AS64269', 'AS43181', 'AS136473'],
    # 'Microsoft': ['AS8812', 'AS8075', 'AS8074', 'AS8073', 'AS8072', 'AS8071', 'AS8069', 'AS8068', 'AS6584', 'AS63314', 'AS63245', 'AS6291', 'AS6194', 'AS6182', 'AS59067', 'AS58862', 'AS5761', 'AS52985', 'AS45139', 'AS400884', 'AS40066', 'AS400582', 'AS400581', 'AS400580', 'AS400579', 'AS400577', 'AS400576', 'AS400575', 'AS400573', 'AS400572', 'AS398961', 'AS398661', 'AS398659', 'AS398658', 'AS398657', 'AS398656', 'AS397996', 'AS397466', 'AS397096', 'AS396463', 'AS395851', 'AS395524', 'AS395496', 'AS36006', 'AS3598', 'AS35106', 'AS32476', 'AS31792', 'AS30575', 'AS30135', 'AS26222', 'AS25796', 'AS23468', 'AS22692', 'AS200517', 'AS20046', 'AS17345', 'AS14719', 'AS13811', 'AS13399', 'AS132348', 'AS12076', 'AS12233', 'AS14271'],
    # 'Microsoft Azure': ['AS14271', 'AS211386', 'AS23536', 'AS24221', 'AS26019', 'AS33447', 'AS397034', 'AS397096', 'AS398100', 'AS398250', 'AS398575', 'AS398656', 'AS398889', 'AS399058', 'AS399583', 'AS400572', 'AS401090', 'AS401093', 'AS401260', 'AS401296'],
    # 'Msn': ['AS34352', 'AS12790'],
    # 'Netflix': ['AS55095', 'AS40027', 'AS394406', 'AS2906', 'AS136292'],
    # 'NextDNS': ['AS34939'],
    # 'Outbrain': ['AS22075'],
    # 'Pinterest': ['AS53620'],
    # 'Quad9': ['AS398892', 'AS398891', 'AS19281'],
    # 'Quora': ['AS36361'],
    # 'Scp': ['AS42404', 'AS210086'],
    # 'Signal': ['AS397755', 'AS60843'],
    # 'Skype': ['AS198097'],
    # 'Slack': ['AS32562', 'AS206770'],
    # 'Smartadserver': ['AS201081', 'AS47043'],
    # 'Snapchat': ['AS395291'],
    # 'Soundcloud': ['AS197157'],
    # 'Spotify': ['AS8403'],
    # 'Stripe': ['AS141743', 'AS394562', 'AS5091', 'AS8838'],
    # 'Tanga': ['AS61933', 'AS202996', 'AS138114', 'AS138109'],
    # 'Tango': ['AS49354', 'AS133415', 'AS10257', 'AS29893', 'AS32717', 'AS48526', 'AS56665'],
    # 'TeamViewer': ['AS43304', 'AS212710', 'AS208187', 'AS208175'],
    # 'Telegram': ['AS62041', 'AS62014', 'AS59930', 'AS44907', 'AS211157'],
    # 'Threema': ['AS29691'],
    # 'Tidal': ['AS10769'],
    # 'Tiktok': ['AS138699'],
    # 'Twitch': ['AS46489', 'AS397153'],
    # 'Twitter': ['AS8945', 'AS63179', 'AS54888', 'AS35995', 'AS13414'],
    # 'Venmo': ['AS25478', 'AS1299', 'AS31133', 'AS50477'],
    # 'Viber': ['AS271336', 'AS207285', 'AS142319'],
    # 'Webex': ['AS9450', 'AS6577', 'AS53258', 'AS399937', 'AS26152', 'AS16472', 'AS152185', 'AS139673', 'AS13445', 'AS10365', 'AS10790', 'AS11615', 'AS9566'],
    # 'Wechat': ['AS140293'],
    # 'Whatsapp': ['AS11917'],
    # 'Yahoo': ['AS7233', 'AS58721', 'AS58720', 'AS58525', 'AS55898', 'AS55517', 'AS55418', 'AS55417', 'AS55416', 'AS45915', 'AS45863', 'AS45502', 'AS45501', 'AS43428', 'AS42173', 'AS40986', 'AS38072', 'AS38045', 'AS34082', 'AS34010', 'AS28122', 'AS265584', 'AS24572', 'AS24506', 'AS24376', 'AS24296', 'AS24236', 'AS24018', 'AS23816', 'AS23663', 'AS204000', 'AS203220', 'AS203219', 'AS203070', 'AS18140', 'AS15896', 'AS15635', 'AS134706', 'AS131898'],
    # 'Youtube': ['AS11344', 'AS1026', 'AS36040', 'AS36561', 'AS43515'],
    # 'Zoom': ['AS46705', 'AS400684', 'AS329157', 'AS31996', 'AS30103', 'AS264449', 'AS205389', 'AS14220', 'AS140430', 'AS139192', 'AS133433', 'AS132998', 'AS264547', 'AS266983', 'AS270225', 'AS31786', 'AS328529', 'AS35433', 'AS36016', 'AS393735', 'AS42611', 'AS62137']
}


"""
for these applications only IP addresses are avaialble
https://bgpview.io/ 
"""
IP = {'deezer': ['185.159.104.0/22', '185.159.106.0/23'],
    'discord': ['188.244.120.0/24', '195.62.89.0/24','198.186.219.0/24' '66.22.192.0/18', '66.22.228.0/24', '66.22.240.0/24', '66.22.244.0/24', ], 
    'snapchat': ['only IPv6 are available'], 
    
}


"""
Applications with ambiguous search keywords on bgpview.io that make ASN lookup difficult.
For example, searching 'line' returns results for airlines, power lines, etc.
"""
GENERIC = {'signal': [],
           'line': [], }

"""
ASN for these applications is not available on the https://radb.mnet database. Need to find more from RIRs
"""
NOT_AVAILABLE =  {'wechat': [],
                  'netnease': [], 
                  'instagram': [],
                  'billibilli': [], 
                  'threema': [],
                  'twitch': [],
                  'bittorent': []
                  }