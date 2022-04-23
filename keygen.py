import sys
from cryptography.fernet import Fernet as fnet


def main(key_ID):
    key_path = "keys/" + key_ID + ".key"
    key = fnet.generate_key()

    with open(key_path, 'wb') as filekey:
        filekey.write(key)


if __name__ == "__main__":
    main(sys.argv[1])
