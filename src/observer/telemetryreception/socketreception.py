import socket

class ObserverSocketReception:
    def __init__(self,file_path):
        self.FILE_PATH=file_path
        # Server configuration
        self.HOST = 'localhost'  # Server IP address
        self.PORT = 12345  # Server port

    def reciever(self):
        # Create a socket object
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind the socket to the specified host and port
        server_socket.bind((self.HOST, self.PORT))

        # Listen for incoming connections
        server_socket.listen(1)

        print("Server is waiting for connections...")

        # Accept a client connection
        client_socket, address = server_socket.accept()
        print(f"Connected to client: {address}")

        # Receive the binary data from the client
        # file_name = client_socket.recv(1024).decode()
        # print(file_name)
        # file_size_str = client_socket.recv(1024).decode()
        # file_size = int(file_size_str)
        # print(file_size)

        # Save the received binary data to a file
        with open(self.FILE_PATH, "wb") as file:
            data = client_socket.recv(1024)
            file.write(data)

        # Close the client connection
        # client_socket.close()

        # Close the server socket
        # server_socket.close()