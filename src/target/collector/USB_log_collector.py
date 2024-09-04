import wmi
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(
    filename='../target_file_pool/usb_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
)

# Initialize the WMI client
c = wmi.WMI()


def log_event(action, device_name, serial_number="N/A"):
    """Logs the USB device event."""
    event_info = f"{action}: {device_name}, Serial Number: {serial_number}"
    logging.info(event_info)
    print(event_info)


def monitor_usb_devices():
    """Monitors USB devices on a Windows machine."""
    print("Monitoring USB devices... Press Ctrl+C to stop.")
    try:
        while True:
            # Listen for USB device connection events
            for usb_device in c.Win32_USBHub():
                device_name = usb_device.Name
                serial_number = getattr(usb_device, 'SerialNumber', 'N/A')
                log_event("Connected", device_name, serial_number)

            # Listen for USB device disconnection events
            watcher = c.watch_for(
                notification_type="Deletion",
                wmi_class="Win32_USBHub"
            )
            device = watcher()
            device_name = device.Name
            serial_number = getattr(device, 'SerialNumber', 'N/A')
            log_event("Disconnected", device_name, serial_number)
    except KeyboardInterrupt:
        print("Stopping USB monitor.")


if __name__ == "__main__":
    monitor_usb_devices()
