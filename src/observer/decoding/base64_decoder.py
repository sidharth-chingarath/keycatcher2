import base64

class Base64Decoding:
    def __init__(self):
        # Path to the binary file
        encoded_base64_binary_file_path = '../observer_file_pool/recieved_file.bin'
        decoded_file_path = '../observer_file_pool/decoded_binary_from_base64_binary.bin'

    def b64_decode_function(self):
        # Read binary data from file
        with open(self.encoded_base64_binary_file_path, 'rb') as file:
            binary_data = file.read()

        # Decode binary data to Base64
        decoded_data = base64.b64decode(binary_data)

        # Write Base64-encoded data to a new file
        with open(self.decoded_file_path, 'wb') as file:
            file.write(decoded_data)
