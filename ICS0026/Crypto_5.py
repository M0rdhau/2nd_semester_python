import random

def commonDenom(a, b):
    if a < b:
        return commonDenom(b, a)
    elif a % b == 0:
        return b
    else:
        return commonDenom(b, a % b)


def keygen(q):
    key = random.randint(10**20, q)
    while commonDenom(q, key) != 1:
        key = random.randint(10**20, q)
    return key


def power(a, b, c):
    x = 1
    y = a
    while b > 0:
        if b % 2 == 0:
            x = (x * y) % c
        y = (y * y) % c
        b = int(b / 2)
    return x % c


def encrypt(msg, q, h, g):
    ct = []
    k = keygen(q)
    s = power(h, k, q)
    p = power(g, k, q)
    for i in range(0, len(msg)):
        ct.append(msg[i])
    print("g^k used= ", p)
    print("g^ak used= ", s)
    for i in range(0, len(ct)):
        ct[i] = s * ord(ct[i])
    return ct, p


def decrypt(ct, p, key, q):
    pt = []
    h = power(p, key, q)
    for i in range(0, len(ct)):
        pt.append(chr(int(ct[i] / h)))
    return pt

a = random.randint(2, 10)
msg = input("Your Message: ")
q = random.randint(10**20, 10**50)
g = random.randint(2, q)
key = keygen(q)
h = power(g, key, q)
print("g= ", g)
print("g^a= ", h)
ct, p = encrypt(msg, q, h, g)
print("Message= ", msg)
print("Encrypted Maessage= ", ct)
d_msg = ''.join(decrypt(ct, p, key, q))
print("Message(Decrypted)= ", d_msg)
