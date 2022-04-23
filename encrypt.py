from cryptography.fernet import Fernet as fnet
import sys


def main(filename, key_ID):
    # read key
    with open(key_ID + ".key", 'rb') as filekey:
        key = filekey.read()

    fernet = fnet(key)  # encryption key

    with open(filename, 'rb') as file:  # read in original file
        original = file.read()

    encrypted = fernet.encrypt(original)  # encrypt

    with open(filename, 'wb') as encrypted_file:  # write back to file as encrypted
        encrypted_file.write(encrypted)




def decrypt(filename, key):
    with open(key + ".key", 'rb') as filekey:
        key = filekey.read()

    fernet = fnet(key)
    with open(filename, 'rb') as file:
        original = file.read()

    decrypt = fernet.decrypt(original)

    with open(filename, 'wb') as encrypted_file:
        encrypted_file.write(decrypt)


if __name__ == "__main__":  # init
    main(sys.argv[1], sys.argv[2])
