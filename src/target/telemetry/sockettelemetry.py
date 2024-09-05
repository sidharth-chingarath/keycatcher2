import socket
import os

FILE_PATH = "../target_file_pool/encrypted_file.bin"

# Server configuration
HOST = 'localhost'  # Receiver's IP address
PORT = 12345        # Receiver's port


# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((HOST, PORT))

# Open the binary file to be sent
with open(FILE_PATH, "rb") as file:
    data = file.read()
file_size = os.path.getsize(FILE_PATH)

# Send the binary data to the server
# client_socket.send("encrypted_file.bin".encode())
# client_socket.send(str(file_size).encode())

client_socket.sendall(data)

# Close the connection
client_socket.close()