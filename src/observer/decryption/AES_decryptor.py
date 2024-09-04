from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
# from ..load_env.my_env import MyENV

key=b'5\x1ey5\xd5\xfeG\xa3\x97\xa0\x1b,\xdb\xe9\xda\xd2'

print("key", key)



# Decrypt the ciphertext
with open("../observer_file_pool/decoded_binary_from_base64_binary.bin", "rb") as file:
    iv = file.read(16)
    ciphertext = file.read()

# Create a new cipher object with the same key and IV
cipher = AES.new(key, AES.MODE_CBC, iv)

# Decrypt the ciphertext
decrypted_data = cipher.decrypt(ciphertext)

# Unpad the decrypted data
unpadded_data = unpad(decrypted_data, AES.block_size)

# Save the decrypted data to a file
with open("../observer_file_pool/decrypted_file.txt", "wb") as file:
    file.write(unpadded_data)