import string

while True:
    plain_text = input("Enter your message:")
    shift = int(input("How many shifts?"))

    alphabet = string.ascii_letters
    shifted = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted)

    encyrpted = plain_text.translate(table)

    print(encyrpted)