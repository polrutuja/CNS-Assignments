from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.exceptions import InvalidSignature

# Generate DSA private key (for signing)
private_key = dsa.generate_private_key(key_size=2048)

# Generate the corresponding public key (for verification)
public_key = private_key.public_key()

# Take user input for the message
message = input("Enter the message to sign: ").encode()

# 1. Signing the message
signature = private_key.sign(
    message,
    hashes.SHA256()
)

print("\nSignature (in bytes):", signature)

# 2. Verifying the signature
try:
    public_key.verify(
        signature,
        message,
        hashes.SHA256()
    )
    print("\nThe signature is valid!")
except InvalidSignature:
    print("\nThe signature is invalid.")
