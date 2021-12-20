from requests import get

cookie = {'WC': '15805988-55406-9hYMjF0rsuI1sb38'}
url = 'https://www.wechall.net/challenge/training/programming1/index.php?action=request'
r = get(url, cookies=cookie)
url = 'https://www.wechall.net/challenge/training/programming1/index.php?answer='
r = get(url + r.text, cookies=cookie)
