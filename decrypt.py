from cryptography.fernet import Fernet as fnet
import sys


def decrypt(filename, key_path):
    with open(key_path, 'rb') as filekey:
        key = filekey.read()

    fernet = fnet(key)
    with open(filename, 'rb') as file:
        original = file.read()

    decrypt = fernet.decrypt(original)

    with open(filename, 'wb') as encrypted_file:
        encrypted_file.write(decrypt)

if __name__ == "__main__":
    decrypt(sys.argv[1], sys.argv[2])