#Encryption
def message():
    msg = "hello mohit this try decrypting this"
    return [msg[i:i + 3] for i in range(0, len(msg), 3)]

chunks = message()
print("Chunked Message =", chunks)

def AsciitoHexa(chunks):
    l = []
    for x in chunks:
        y = "".join([hex(ord(ch)) for ch in x])
        l.append(y.replace("0x", ""))
    return l

hexa_list = AsciitoHexa(chunks)
print("Hexadecimal value =", hexa_list)

def HextoInteger(hexa_list):
    l = [int(a, 16) for a in hexa_list]
    return l

def squaremultiply(y1, e, N):
    b = 1
    while e > 0:
        if e % 2 != 0:
            b = (b*y1)%N
        y1 = (y1*y1)%N
        e = int(e/2)
    return b % N

def encryption(str,N,e):
    x = []
    for i in integer_lis:
        x.append(squaremultiply(i, N, e))
    return x

integer_lis = HextoInteger(hexa_list)
encr_lis = encryption(integer_lis, 633382541, 2447280851)
print("Encrypted text =", encr_lis)
