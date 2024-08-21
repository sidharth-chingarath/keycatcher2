import base64

# Path to the binary file
file_path = '../target_file_pool/encrypted_file.bin'
destination_path = '../target_file_pool/encoded_base64_binary_for_email.bin'


# Encode file in Base64
with open(file_path, 'rb') as file:
    binary_data = file.read()

encoded_data = base64.b64encode(binary_data)

with open(destination_path,'wb') as write_file:
    write_file.write(encoded_data)



# The encoded_data can now be sent via email
