import hashlib
import uuid


def hash(inp_str: str):
    salt = uuid.uuid4().hex
    hashed_password = hashlib.sha256((inp_str + salt).encode('utf-8'))
    return salt, hashed_password.hexdigest()


if __name__ == "__main__":
    password = "abc"
    hashed_password = hash(password)
    print("password:\t", password, "\nsalt:\t", hashed_password[0], "\nhash: ", hashed_password[1])
