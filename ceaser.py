import string


plain_text = input("normal caesar cipher: ")
print(plain_text)

alphabet = string.ascii_lowercase
shift = 1
shifted = alphabet[shift:] + alphabet[:shift]

table = str.maketrans(alphabet, shifted)

encrypted = plain_text.translate(table)

print(encrypted)