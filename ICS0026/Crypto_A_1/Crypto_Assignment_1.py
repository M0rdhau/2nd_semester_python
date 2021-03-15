from binascii import hexlify, unhexlify
from Crypto.Cipher import AES
import hashlib
import base64

iv = str.encode(16 * '\x00')



def encrypt():
    path = input("Select which image to encode: ")
    key = input("Enter the key: ")
    writepath = input("Enter file to write in: ")
    with open(path, 'rb') as f:
        content = f.read()
    hexcode = hexlify(content)
    generatedKey =  hashlib.sha256(str.encode(key)).digest()
    cipher = AES.new(generatedKey, AES.MODE_CBC, iv)
    hexcode = hexcode + b'0'*(16 - len(hexcode)%16)
    encrypted = cipher.encrypt(hexcode)
    result = base64.b64encode(encrypted)
    with open(writepath, 'wb') as file:
        file.write(result)


def decrypt():
    key = input("Enter the key: ")
    path = input("Enter file to decode: ")
    writepath = input("Enter file to write in: ")
    with open(path, 'rb') as f:
        message = f.read()
    generatedKey =  hashlib.sha256(str.encode(key)).digest()
    cipher = AES.new(generatedKey, AES.MODE_CBC, iv)
    encrypt_bytes = base64.b64decode(message)
    decrypt_bytes = cipher.decrypt(encrypt_bytes)
    with open(writepath, 'wb') as file:
        file.write(unhexlify(decrypt_bytes))

def main():
    num = input("Which action would you like to take:\n1. Encrypt\n2. Decrypt\n3. Exit\n")
    if num == "1":
        encrypt()
        main()
    elif num == "2":
        decrypt()
        main()
    elif num == "3":
        exit()
    else:
        print("Wrong number!")
        main()


main()