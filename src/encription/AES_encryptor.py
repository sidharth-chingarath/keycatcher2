from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# Generate a random key (16 bytes for AES-128)
key = get_random_bytes(16)

# Open the text file to be encrypted
with open("original_file.txt", "rb") as file:
    data = file.read()

# Pad the data to a multiple of 16 bytes
padded_data = pad(data, AES.block_size)

# Create a cipher object with the key and mode of operation
cipher = AES.new(key, AES.MODE_CBC)

# Encrypt the padded data
ciphertext = cipher.encrypt(padded_data)

# Save the IV (initialization vector) along with the ciphertext
with open("encrypted_file.bin", "wb") as file:
    file.write(cipher.iv)
    file.write(ciphertext)

# Decrypt the ciphertext
with open("encrypted_file.bin", "rb") as file:
    iv = file.read(16)
    ciphertext = file.read()

# Create a new cipher object with the same key and IV
cipher = AES.new(key, AES.MODE_CBC, iv)

# Decrypt the ciphertext
decrypted_data = cipher.decrypt(ciphertext)

# Unpad the decrypted data
unpadded_data = unpad(decrypted_data, AES.block_size)

# Save the decrypted data to a file
with open("decrypted_file.txt", "wb") as file:
    file.write(unpadded_data)