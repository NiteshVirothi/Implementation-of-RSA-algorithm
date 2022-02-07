def signature():
    sign = "NiteshVirothi"
    return [sign[i:i + 3] for i in range(0, len(sign), 3)]

chunk = signature()
print("Chunked Message =", chunk)

def AsciitoHexa(chunk):
    l = []
    for j in chunk:
        var = "".join([hex(ord(ch)) for ch in j])
        l.append(var.replace("0x", ""))
    return l

hexa = AsciitoHexa(chunk)
print("Hexadecimal values =", hexa)

def HextoInteger(hexa):
    l = [int(x, 16) for x in hexa]
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
    for i in integer:
        x.append(squaremultiply(i, N, e))
    return x

integer = HextoInteger(hexa)
print("Integer value of signature =", integer)

encr_lis = encryption(integer, 2069374087, 2541110441)
print("Encrypted sign =", encr_lis)