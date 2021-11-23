import hashlib
import secrets


class SecretPassword:

    SALT = secrets.token_bytes(32)

    @classmethod
    def password_encrypt(cls, password: str):
        """ encrypt password"""

        if password != "":
            return str(hashlib.pbkdf2_hmac(
                "sha256",
                password.encode("utf-8"),
                cls.SALT, 4096
            ))

    @classmethod
    def password_verify(cls, hash_password: str, password: str):
        """ verify valid password"""

        hashed_pw_verify = str(hashlib.pbkdf2_hmac(
            "sha256",
            password.encode("utf-8"),
            cls.SALT, 4096
        ))

        if not secrets.compare_digest(
            hash_password,
            hashed_pw_verify
        ):
            return False

        return True
