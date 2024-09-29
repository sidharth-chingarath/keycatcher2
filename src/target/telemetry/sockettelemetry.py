import socket
import os

class TargetSocketTelemetry:
    def __init__(self,file_path):
        self.FILE_PATH = file_path
        # Server configuration
        self.HOST = 'localhost'  # Receiver's IP address
        self.PORT = 12345  # Receiver's port

    def sender(self):
        # Create a socket object
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to the server
        client_socket.connect((self.HOST, self.PORT))

        # Open the binary file to be sent
        with open(self.FILE_PATH, "rb") as file:
            data = file.read()
        file_size = os.path.getsize(self.FILE_PATH)

        # Send the binary data to the server
        # client_socket.send("encrypted_file.bin".encode())
        # client_socket.send(str(file_size).encode())

        client_socket.sendall(data)

        # Close the connection
        # client_socket.close()