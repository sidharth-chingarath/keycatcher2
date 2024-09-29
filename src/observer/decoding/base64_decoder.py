import base64

class Base64Decoding:
    def __init__(self,recieved_file_path,decoded_file_path):
        # Path to the binary file
        self.encoded_base64_binary_file_path = recieved_file_path
        self.decoded_file_path = decoded_file_path

    def b64_decode_function(self):
        # Read binary data from file
        with open(self.encoded_base64_binary_file_path, 'rb') as file:
            binary_data = file.read()

        # Decode binary data to Base64
        decoded_data = base64.b64decode(binary_data)

        # Write Base64-encoded data to a new file
        with open(self.decoded_file_path, 'wb') as file:
            file.write(decoded_data)
