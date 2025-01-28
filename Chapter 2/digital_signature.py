import hashlib
import rsa

def dig_sign(message, private_key):
    hashed = hashlib.sha256(message.encode()).digest()
    signature = rsa.sign(hashed, private_key, 'SHA-256')

    return signature

def verify_sign(message, signature, public_key):
    hashed = hashlib.sha256(message.encode()).digest()
    
    try:
        rsa.verify(hashed, signature, public_key)
        print("signature is valid")
    except rsa.VerificationError:
        print("signature is invalid")

public_key, private_key = rsa.newkeys(512)
message = "attack from the left"

print(public_key)
print(private_key)
signature = dig_sign(message, private_key)
print(f"Digital Signature : {signature.hex()}")

verify_sign(message, signature, public_key)