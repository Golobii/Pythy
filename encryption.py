import random


def generate_key():
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = lower.upper()
    numbers = "1234567890"
    symbols = "!\"#$%&/()=?*"

    all = lower + upper + numbers + " " + symbols
    str_var = list(all)
    random.shuffle(str_var)
    key = ''.join(str_var)
    with open("secret", "w") as key_file:
        key_file.write(key)


def load_key():
    generate_key()
    f = open("secret", "r").read()
    return f
    f.close()


def encrypt(key, string):
    encrypted_string = ''
    for i in string:
        pos = key.find(i)
        pos = pos - 5
        encrypted_string += key[pos]
    return encrypted_string


def decrypt(key, encrypted_string):
    decrypted_string = ''
    for i in encrypted_string:
        x = random.randint(0, len(key) - 1)
        try:
            pos = key.find(i)
            pos = pos + 5
            if pos > (len(key) - 1):
                pos = pos - len(key)
            decrypted_string += key[pos]
        except IndexError:
            print(x)
            decrypted_string += key[x]
    return decrypted_string


# key = load_key()
# print(key)

# string = input("Enter your message here:")

# encrypted_string = encrypt(key, string)
# print(encrypted_string)

# while True:
#     key = input("Enter the decryption key here: ")
#     decrypted_string = decrypt(key, encrypted_string)
#     print(decrypted_string)
