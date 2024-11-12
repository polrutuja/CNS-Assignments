
# RSA Algorithm in Python

import random
from sympy import mod_inverse

# Step 1: Key Generation
def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose e such that 1 < e < phi and gcd(e, phi) = 1
    e = random.randrange(1, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(1, phi)

    # Calculate d (modular inverse of e)
    d = mod_inverse(e, phi)

    # Public and private key pairs
    return ((e, n), (d, n))

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Step 2: Encryption
def encrypt(public_key, plaintext):
    e, n = public_key
    # Convert plaintext to integers
    cipher = [(ord(char) ** e) % n for char in plaintext]
    return cipher

# Step 3: Decryption
def decrypt(private_key, ciphertext):
    d, n = private_key
    # Convert integers back to characters
    plain = [chr((char ** d) % n) for char in ciphertext]
    return ''.join(plain)

# Example usage
if __name__ == '__main__':
    p = 61  # First prime number
    q = 53  # Second prime number
    public, private = generate_keypair(p, q)
    
    print("Public key:", public)
    print("Private key:", private)
    
    message = "Hello"
    encrypted_msg = encrypt(public, message)
    print("Encrypted message:", encrypted_msg)
    
    decrypted_msg = decrypt(private, encrypted_msg)
    print("Decrypted message:", decrypted_msg)
