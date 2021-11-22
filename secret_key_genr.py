#!python3

import os
from uuid import uuid4
from secrets import token_urlsafe

urandom_delimiter = os.urandom(12)
secret_key_generate_oub = uuid4().hex
urlsafe_token = token_urlsafe(12)

print(
    urandom_delimiter,
    secret_key_generate_oub,
    urlsafe_token
)