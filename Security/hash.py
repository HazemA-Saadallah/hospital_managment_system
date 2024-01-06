import hashlib
import uuid


def genrate_hash_and_salt(inp_str: str):
    salt = uuid.uuid4().hex
    hashed_password = hashlib.sha256((inp_str + salt).encode('utf-8'))
    return salt, hashed_password.hexdigest()


def hash(password: str, salt: str):
    hashed_password = hashlib.sha256((password + salt).encode('utf-8'))
    return hashed_password.hexdigest()


if __name__ == "__main__":
    password = input("Enter the password: ")
    hashed_password = genrate_hash_and_salt(password)
    print("password:\t\t", password, "\nsalt:\t\t\t", hashed_password[0], "\nhash:\t\t\t", hashed_password[1])
    print("test hash function:\t", hash(password, hashed_password[0]))
