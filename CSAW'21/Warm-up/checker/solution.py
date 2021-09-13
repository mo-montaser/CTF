def reverse_up(b_string):
    x = []
    y = 8
    for i in range(len(b_string)//8):
        x.append(chr(int(b_string[i*y:i*y+8],2)//2))

    return "".join(x)

def reverse_down(b_string):
    x = list(b_string)
    for i in range(len(x)):
        if(x[i] == '0'):
            x[i] = '1'
        else:
            x[i] = '0'

    return "".join(x)

def reverse_right(b_string,d):
    x = b_string[len(b_string)-d:] + b_string[0:len(b_string)-d]
    return x

def reverse_left(b_string,d):
    x = b_string[::-1]
    x = reverse_right(x,len(x)-d)
    return x

def decode(encoded_string):
    d = 24
    x = reverse_left(encoded_string,d)
    x = reverse_down(x)
    x = reverse_right(x,d)
    x = reverse_up(x)
    return x

encoded_string = "1010000011111000101010101000001010100100110110001111111010001000100000101000111011000100101111011001100011011000101011001100100010011001110110001001000010001100101111001110010011001100"

print(decode(encoded_string))
