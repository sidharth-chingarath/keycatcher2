from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
# from dotenv import load_dotenv
# import os

# Load environment variables from .env file
# load_dotenv()

# Generate a random key (16 bytes for AES-128)
# key = get_random_bytes(16)
# key=os.getenv("CRYPTO_PRIVATE_KEY")
key=b'5\x1ey5\xd5\xfeG\xa3\x97\xa0\x1b,\xdb\xe9\xda\xd2'
print("Key", key)
# with open("../decryption/key.txt","w") as key_file:
#     key_file.write(str(key))
# Open the text file to be encrypted
with open("../target_file_pool/keylog.txt", "rb") as file:
    data = file.read()

for i in data:
    print(i)
# Pad the data to a multiple of 16 bytes
padded_data = pad(data, AES.block_size)

# Create a cipher object with the key and mode of operation
cipher = AES.new(key, AES.MODE_CBC)

# Encrypt the padded data
ciphertext = cipher.encrypt(padded_data)

# Save the IV (initialization vector) along with the ciphertext
with open("../target_file_pool/encrypted_file.bin", "wb") as file:
    file.write(cipher.iv)
    file.write(ciphertext)