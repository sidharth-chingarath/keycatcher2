import base64

# Path to the binary file
encoded_base64_binary_file_path = '../observer_file_pool/recieved_base64_encoded_binary.bin'
decoded_file_path = '../observer_file_pool/decoded_binary_from_base64_binary.bin'

# Read binary data from file
with open(encoded_base64_binary_file_path, 'rb') as file:
    binary_data = file.read()

# Decode binary data to Base64
decoded_data = base64.b64decode(binary_data)

# Write Base64-encoded data to a new file
with open(decoded_file_path, 'wb') as file:
    file.write(decoded_data)
