import socket
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.exceptions import InvalidSignature

# Set up server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 65432))  # Bind to localhost, port 65432
server_socket.listen(1)

print("Server is listening...")

# Accept connection from client
conn, addr = server_socket.accept()
print(f"Connected by {addr}")

# Receive data from the client
data = conn.recv(4096)  # Adjust buffer size as needed
public_bytes, message, signature = data.split(b"||")

# Deserialize the public key
public_key = serialization.load_pem_public_key(public_bytes)

# Verify the signature
try:
    public_key.verify(signature, message, ec.ECDSA(hashes.SHA256()))
    print(signature)
    print("Signature is valid. Message verified.")
except InvalidSignature:
    print("Signature is invalid. Message verification failed.")

conn.close()
server_socket.close()
