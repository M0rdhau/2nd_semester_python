def oneTimePad():
    message = input('Enter a message to encrypt(or decrypt): ')
    key = int(input('Enter a one-byte key to encrypt with(in binary): '), 2)

    encryptedBinary = ''

    for i in message:
        encrypted = ord(i) ^ key
        encryptedBinary += str(format(encrypted, 'b'))

    print('encrypted message is(in Binary): ' + encryptedBinary)

def vigener(encrypt):
    if encrypt:
        somemessage = 'encrypt'
    else:
        somemessage = 'decrypt'
    message = str.upper(input('Enter a message to ' + somemessage + ': '))
    key = input('Enter a key to encrypt with: ')

    encryptedMessage = ''

    if encrypt:
        for i, j in zip(message, key):
            print(i + ' is ' + str(ord(i)))
            encrypted = ((ord(i) - 65) + (ord(j) - 65)) % 26
            encryptedMessage += chr(encrypted + 65)
    else:
        for i, j in zip(message, key):
            print(i + ' is ' + str(ord(i)))
            encrypted = ((ord(i) - 65) - (ord(j) - 65)) % 26
            encryptedMessage += chr(encrypted + 65)

    print('encrypted message is: ' + encryptedMessage)

def initScript():
    print('Would you like to encrypt using vigener cipher(1) or one time pad(2)? Type 0 to quit')
    which = int(input('Enter a number: '))
    while(which != 0):
        if (which == 1):
            print('Would you like to encrypt(1) or decrypt(2) a message?')
            yesno = int(input('Enter a number: '))
            if (yesno == 1):
                vigener(True)
            else:
                vigener(False)
        elif (which == 2):
            oneTimePad()
        else:
            print('Wrong number!')

        which = int(input('Would you like to repeat? type 1 or 2. 0 to exit'))

initScript()