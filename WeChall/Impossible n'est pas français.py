from re import compile
import requests

url_1 = 'https://www.wechall.net/challenge/impossible/index.php?request=new_number'
url_2 = 'https://www.wechall.net/challenge/impossible/index.php'
cookie = {'WC': '15824987-55406-HjKeTspdp11CCbqJ'}

# get a new number
r = requests.post(url_1, cookies=cookie)

# send wrong number
data = {'solution': 99}
r = requests.post(url_2, data=data, cookies=cookie)
number = compile(r'(\d{20,})').findall(r.text)[0]

# send the correct answer
data = {'solution': number}
r = requests.post(url_2, data=data, cookies=cookie)
