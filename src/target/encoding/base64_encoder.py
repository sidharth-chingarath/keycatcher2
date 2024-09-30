import base64
from src.target.res.Resources import Res

class Base64Encoding:
    def __init__(self):
        # Path to the binary file
        res_instance = Res()
        self.file_path = res_instance.resource_path('./target_file_pool/encrypted_file.bin')
        self.destination_path = res_instance.resource_path('./target_file_pool/encoded_base64_binary_for_email.bin')

    def b64_encode_function(self):
        # Encode file in Base64
        with open(self.file_path, 'rb') as file:
            binary_data = file.read()

        encoded_data = base64.b64encode(binary_data)

        with open(self.destination_path, 'wb') as write_file:
            write_file.write(encoded_data)

