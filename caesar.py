def encrypt(text,shift):
    text= text.lower()
    encrypted_text=""
    for char in text:
        if char.islower():
            encrypted_text+=chr((ord(char)+shift-97)% 26+97)
        else:
            encrypted_text+=char
    return encrypted_text


originalmessage ="Encryption"
encryptedmessage=encrypt(originalmessage,2)
print(encryptedmessage)