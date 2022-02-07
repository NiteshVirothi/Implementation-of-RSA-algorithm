v = "Mohit Kumar"
def verify(x, e , N):
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

x = [67494228,1228104877,280401180,1778613282]
verified_sign = verify(x, 633382541, 2447280851)
a = list()
b = [hex(i) for i in verified_sign]
for i in b:
    a.append(i.replace("0x", ""))
print("Hexadecimal values =", a)

c = [bytearray.fromhex(i).decode() for i in a]
print("chunked Message =", c)

dec_msg = "".join(c)
print("Decrypted message from partner is =", dec_msg)
if v == dec_msg:
    print("Signature is Valid")
else:
    print("signature is not Valid")