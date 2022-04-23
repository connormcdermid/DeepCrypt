from cryptography.fernet import Fernet as fnet
import sys


def main(filename, key_ID):
    # read key
    with open(key_ID + ".key", 'rb') as filekey:
        key = filekey.read()

    fernet = fnet(key)

    with open(filename, rb) as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open(filename, wb) as encrypted_file:
        encrypted_file.write(encrypted)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
