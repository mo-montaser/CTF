from base64 import b64decode, b64encode
import requests


def bitFlip(pos, bit, data):
    list1 = list(b64decode(data).decode())
    list1[pos] = chr(bit)
    list1 = ''.join(list1).encode()
    return b64encode(list1).decode()


cookie = 'dFdaVm42cjJpY3cvclhlZ3EvY1NFV3Y0VzFnY3owR1pKY0E4dXptY2pBd3ZTVnBuODNDWlpOdGIraHBLZ3N2WXA3RlFRTXd2SWRqNVI5cUtUL2FKd0liL21vNEV0ditrcnJNZU1rVzIzWjJmQnhxcml6QnJNSnM2RFlqcnJlTUs='
for i in range(128):
    for j in range(128):
        ck = bitFlip(i, j, cookie)
        cookies = {'auth_name': ck}
        url = 'http://mercury.picoctf.net:34962/'
        r = requests.get(url, cookies=cookies)
        if 'picoCTF{' in r.text:
            print(r.text)
            break
        else:
            print(j)
