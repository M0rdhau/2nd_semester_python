from Crypto.Cipher import AES
from binascii import hexlify, unhexlify

keystring = 'c8141916f19939915f5b8c5870898d2c'
vectorstring = 'ed15f24f2bf5936629c8ef1b33e2d3c3'
plainstring1 = '3f608b127713127939d867db7c1c31b7'
plainstring2 = '87db275e14765e9549dff8af8096e0ef'
plainstring3 = 'ae75c44d760c781cebf5a270a2e4795f'

keyhex = unhexlify(keystring)
vectorhex = unhexlify(vectorstring)
plain1 = unhexlify(plainstring1)
plain2 = unhexlify(plainstring2)
plain3 = unhexlify(plainstring3)

encryption = AES.new(keyhex, AES.MODE_CBC, vectorhex)
ciphertext = encryption.encrypt(plain1 + plain2 + plain3)
print(hexlify(ciphertext))
deciphered = AES.new(keyhex, AES.MODE_CBC, vectorhex)
plain = deciphered.decrypt(ciphertext)
print(plain == plain1 + plain2 + plain3)
print(hexlify(plain))