#!python3

from hashlib import blake2b
from hmac import compare_digest


class SecretPassword:

    SECRET_KEY = b'password_hashSecretKey'
    AUTH_SIZE = 20

    @classmethod
    def password_encrypt(cls, password: str):
        """ encrypt password"""

        if password != "":

            hash_blake = blake2b(digest_size=cls.AUTH_SIZE, key=cls.SECRET_KEY)
            hash_blake.update(password.encode())
            return hash_blake.hexdigest().encode('utf-8')

    @classmethod
    def password_verify(cls, password: str, hash_password: bytes):
        """ verify valid password"""

        password_genr = cls.password_encrypt(password)

        if not compare_digest(password_genr, hash_password):
            return False

        return True


# def genewrite_key():
#     key= Fernet.generate_key()
#     with open("pass.key","wb") as key_file:
#         key_file.write(key)

# def get_key():
#     key= open("pass.key","rb").read()
#     return key


# genewrite_key()
# msg = "antonio"
# text = msg.encode()

# key = get_key()

# a = Fernet(key)

# encrypted_msg= a.encrypt(text)

# print(encrypted_msg)

# decoded_text = a.decrypt(onlocal)
# print(decoded_text)


# First Sucess
# key_ppwd = b'bXlfcGFzc3dvcmQ='
# password = "my_password".encode("utf-8")

# encoded = base64.b64encode(password)
# #print(encoded)

# decoded = base64.b64decode(key_ppwd)
# print(decoded)
