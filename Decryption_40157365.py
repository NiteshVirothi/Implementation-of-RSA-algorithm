def decryption(x, e , N):
    y = []
    for i in x:
        y.append(squaremultiply(i, e, N))
    return y

def squaremultiply(y1, e, N):
    b = 1
    while e > 0:
        if e % 2 != 0:
            b = (b*y1)%N
        y1 = (y1*y1)%N
        e = int(e/2)
    return b % N

x = [229750177, 1229262504,170559932,2427021921,32915142,2353489820,1551450868,2412748639,80631827,117195144]
dec_message = decryption(x, 2069374087, 2541110441)
a  = list()
b = [hex(i) for i in dec_message]
for j in b:
    a.append(j.replace("0x", ""))
print("Hexadecimal values =", a)

c = [bytearray.fromhex(i).decode() for i in a]
print("Chunked Message =", c)

decrypt_message = "".join(c)
print("Decrypted message from partner is =", decrypt_message)