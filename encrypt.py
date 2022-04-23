from cryptography.fernet import Fernet as fnet
import sys


def encrypt(filename, key_path):
    # read key
    with open(key_path, 'rb') as filekey:
        key = filekey.read()

    fernet = fnet(key)  # encryption key

    with open(filename, 'rb') as file:  # read in original file
        original = file.read()

    encrypted = fernet.encrypt(original)  # encrypt

    with open(filename, 'wb') as encrypted_file:  # write back to file as encrypted
        encrypted_file.write(encrypted)






if __name__ == "__main__":  # init
    encrypt(sys.argv[1], sys.argv[2])
