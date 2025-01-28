import hashlib

sha_256 = hashlib.sha256()

message = b"Hello Brother"

sha_256.update(message)

digest = sha_256.digest()

hexdigest = digest.hex()

print(hexdigest)