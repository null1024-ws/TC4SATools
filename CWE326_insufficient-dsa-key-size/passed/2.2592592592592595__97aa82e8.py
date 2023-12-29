from cryptography.hazmat import backends
from cryptography.hazmat.primitives.asymmetric import dsa

key_size = int('1024')
dsa.generate_private_key(key_size=key_size, backend=backends.default_backend())