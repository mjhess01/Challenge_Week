def caesar_cipher():
    phrase = str(input("Encode phrase: "))
    x = ''
    num = int(input("How many letters? "))
    for letter in phrase:
        x += chr(ord(letter) + num)
    print(x)

caesar_cipher()

def caesar_cipher_dec():
    phrase = str(input("Decode phrase: "))
    x = ''
    num = int(input("How many letters? "))
    for letter in phrase:
        x += chr(ord(letter) + num)
    print(x)

caesar_cipher_dec()