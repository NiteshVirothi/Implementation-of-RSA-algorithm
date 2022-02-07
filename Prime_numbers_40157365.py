import math
import sympy

def Random_primenumber(a,b):
    p = sympy.randprime(a,b)
    q = sympy.randprime(a,b)
    print("\n1st Prime number p =",p)
    print("2nd Prime number q =",q)
    n = p*q
    print("\nN = p*q =", n)
    phi = (p-1)*(q-1)
    print("Φ(n) = (p-1)*(q-1) =", phi)
    return phi
phi = Random_primenumber(32768, 65536)

def Encryption_key():
    e = sympy.randprime(11, phi/2)
    while e < phi:
        if math.gcd(e, phi)==1:
            e_key = e
            break
        e = sympy.randprime(11, phi/2)
    return e_key

def gcd(x,y):
    if x == 0:
        return (y, 0, 1)
    else:
        g, b1,a1 = gcd(y % x, x)
        return (g, a1-(y//x) * b1,b1)

def inversemod(a, m):
    g, a1, b1 = gcd(a, m)
    if g != 1:
        raise Exception('inverse not possible')
    else:
        return a1 % m

encrypt_key = Encryption_key()
print("\nThe encryption key 'e' is =",encrypt_key)

decrypt_key = inversemod(encrypt_key, phi)
print(f"The decryption key 'd' is =",decrypt_key)