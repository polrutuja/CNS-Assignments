# Hillman la client server communication karaycha ahe with 2 programs or 2 different pcs
import random

# Function to perform modular exponentiation (base^exp) % mod
def modular_exponentiation(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:  # If exp is odd, multiply base with result
            result = (result * base) % mod
        exp = exp >> 1  # Right shift exp by 1 (divide by 2)
        base = (base * base) % mod  # Change base to base^2 % mod
    return result

# Diffie-Hellman Key Exchange
def diffie_hellman():
    # Publicly known values (these should be agreed upon by both parties)
    p = 23  # Prime number (modulus)
    g = 5   # Primitive root modulo p (base)

    # Party A (Alice) chooses a private key
    private_key_a = random.randint(1, p-1)
    public_key_a = modular_exponentiation(g, private_key_a, p)

    # Party B (Bob) chooses a private key
    private_key_b = random.randint(1, p-1)
    public_key_b = modular_exponentiation(g, private_key_b, p)

    print(f"Alice's Public Key: {public_key_a}")
    print(f"Bob's Public Key: {public_key_b}")

    # Alice and Bob exchange public keys and calculate the shared secret
    shared_secret_a = modular_exponentiation(public_key_b, private_key_a, p)  # Alice calculates the shared secret
    shared_secret_b = modular_exponentiation(public_key_a, private_key_b, p)  # Bob calculates the shared secret

    print(f"Alice's Calculated Shared Secret: {shared_secret_a}")
    print(f"Bob's Calculated Shared Secret: {shared_secret_b}")

    # The shared secret should be the same for both Alice and Bob
    assert shared_secret_a == shared_secret_b, "Shared secrets do not match!"
    print(f"Shared Secret (Common Key): {shared_secret_a}")

# Example usage
if __name__ == "__main__":
    diffie_hellman()
