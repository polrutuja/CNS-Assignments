import socket
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes, serialization

# Generate a private key for the client
private_key = ec.generate_private_key(ec.SECP256R1())
public_key = private_key.public_key()

# Serialize the public key to send to the server
public_bytes = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Message to sign
message = b"Hello, this is a message from the client."

# Sign the message using the private key
signature = private_key.sign(message, ec.ECDSA(hashes.SHA256()))

# Establish socket connection with the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 65432))  # Connect to server on localhost, port 65432

# Send the serialized public key, message, and signature to the server
client_socket.sendall(public_bytes + b"||" + message + b"||" + signature)

print("Message and signature sent to server.")

client_socket.close()
