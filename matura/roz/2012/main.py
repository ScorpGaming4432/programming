def encode(text, key):
    out = ''
    for i in range(len(text)):
        value = ord(text[i]) + ord(key[i%len(key)]) - 64
        if value > 90:
            value -= 26
        out += chr(value)
    return out

def decode(code, key):
    out = ''
    for i in range(len(code)):
        value = ord(code[i]) - ord(key[i%len(key)]) + 64
        if value < 65:
            value += 26
        out += chr(value)
    return out


with open('tj.txt') as file0, open('klucze1.txt') as file1, open('sz.txt') as file2, open('klucze2.txt') as file3:
    out = [[], []]
    file0 = file0.readlines()
    file1 = file1.readlines()
    file2 = file2.readlines()
    file3 = file3.readlines()
    for i in range(len(file0)):
        file0[i] = file0[i].rstrip()
        file1[i] = file1[i].rstrip()
        file2[i] = file2[i].rstrip()
        file3[i] = file3[i].rstrip()
        out[0].append(encode(file0[i], file1[i]))
        out[1].append(decode(file2[i], file3[i]))
print(out)
