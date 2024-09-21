from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
# from ..load_env.my_env import MyENV


class AESDecription:
    def __init__(self,decoded_file_path,decrypted_file_path) -> None:
        self.write_path=decrypted_file_path
        self.read_path=decoded_file_path

    def decryption_method(self):
        key=b'5\x1ey5\xd5\xfeG\xa3\x97\xa0\x1b,\xdb\xe9\xda\xd2'
        print("key", key)
        # Decrypt the ciphertext
        with open(self.read_path, "rb") as file:
            iv = file.read(16)
            ciphertext = file.read()

        # Create a new cipher object with the same key and IV
        cipher = AES.new(key, AES.MODE_CBC, iv)

        # Decrypt the ciphertext
        decrypted_data = cipher.decrypt(ciphertext)

        # Unpad the decrypted data
        unpadded_data = unpad(decrypted_data, AES.block_size)

        # Save the decrypted data to a file
        with open(self.write_path, "wb") as file:
            file.write(unpadded_data)