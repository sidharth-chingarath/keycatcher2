from telemetryreception.socketreception import ObserverSocketReception
from decoding.base64_decoder import Base64Decoding
from decryption.AES_decryptor import AESDecription
from time import sleep
class Main:
    def __init__(self) -> None:
        self.time_seconds=1
        self.receved_file="./observer_file_pool/recieved_file.bin"
        self.decoded_file='./observer_file_pool/decoded_binary_from_base64_binary.bin'
        self.decrypted_file = "./observer_file_pool/decrypted_file.txt"
    def main_function(self):
        # socket telemetry reception
        reception_instance = ObserverSocketReception(self.receved_file)
        reception_instance.reciever()
        sleep(self.time_seconds)
        # Decoding
        decoding_instance=Base64Decoding(self.receved_file,self.decoded_file)
        decoding_instance.b64_decode_function()
        sleep(self.time_seconds)
        # Decryption
        decryption_instance=AESDecription(self.decoded_file,self.decrypted_file)
        decryption_instance.decryption_method()
        print("end of observer main function")
        return None
    
main=Main()
main.main_function()