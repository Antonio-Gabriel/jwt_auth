#!python3

import os
from uuid import uuid4

urandom_delimiter = os.urandom(12)
secret_key_generate_oub = uuid4.uuid4().hex

print(
    urandom_delimiter,
    secret_key_generate_oub
)