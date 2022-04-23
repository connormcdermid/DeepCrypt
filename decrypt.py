from cryptography.fernet import Fernet as fnet
import sys


def decrypt(filename, key):
    with open(key + ".key", 'rb') as filekey:
        key = filekey.read()

    fernet = fnet(key)
    with open(filename, 'rb') as file:
        original = file.read()

    decrypt = fernet.decrypt(original)

    with open(filename, 'wb') as encrypted_file:
        encrypted_file.write(decrypt)