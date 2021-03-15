from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from Crypto import Random
import base64


def generate_key():
    name = input("Enter filename: ")
    sizeNum = input("Enter size of the key 1. 1024; 2. 2048; 3. 3072; \n")
    if sizeNum == '1':
        size = 1024
    elif sizeNum == '2':
        size = 2048
    elif sizeNum == '3':
        size = 3072
    else:
        print("Wrong number!")
        return
    print(size)
    key = RSA.generate(size)
    pub_file = open(name, "w+")
    pub_file.write(key.export_key().decode("ascii"))
    pub_file.close()

    priv_file = open(name + ".pub", "w+")
    priv_file.write(key.publickey().export_key().decode("ascii"))
    priv_file.close()

def encrypt():
    path = input("Enter public key path: ")
    with open(path) as privatefile:
        keydata = privatefile.read()
    cipher_pub = PKCS1_v1_5.new(RSA.importKey(keydata))
    secret_byte = cipher_pub.encrypt(input("Enter plaintext: ").encode())

    print(base64.b64encode(secret_byte))


def decrypt():
    path = input("Enter private key path: ")
    with open(path) as privatefile:
        keydata = privatefile.read()
    cipher_priv = PKCS1_v1_5.new(RSA.importKey(keydata))
    byte = cipher_priv.decrypt(base64.b64decode(input("Enter BASE64 ciphertext: ")), Random.new().read(15))

    print(byte.decode())


def main():
    num = input("Which action would you like to take:\n1. Generate key pair\n2. Encrypt\n3. Decrypt\n4. Exit\n")
    if num == "1":
        generate_key()
        main()
    elif num == "2":
        encrypt()
        main()
    elif num == "3":
        decrypt()
        main()
    elif num == "4":
        exit()
    else:
        print("Wrong number!")
        main()


main()
