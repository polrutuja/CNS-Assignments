import hashlib

# Take user input for the text
text = input("Enter the text to hash: ")

# Create a SHA-1 hash object
sha1_hash = hashlib.sha1()

# Update the hash object with the text (encoded to bytes)
sha1_hash.update(text.encode())

# Get the hexadecimal representation of the digest
digest = sha1_hash.hexdigest()

print("SHA-1 Digest:", digest)
