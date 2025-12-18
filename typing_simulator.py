import random
import time
import keyboard

########## Balance Spending ###########
MESSAGES = [
    "message 1",
    "message 2",
    "message 3",
]


# Index to track the next message.
message_index = 0


def type_message(message: str) -> None:
    """
    Simulate human-like typing by writing each character with a random delay,
    and add occasional extra pauses to mimic natural pauses.
    """
    time.sleep(1)
    for char in message:
        keyboard.write(char)
        # Regular keystroke delay.
        time.sleep(random.uniform(0.05, 0.15))

        # If the character is punctuation, add a longer pause.
        if char in [".", ",", "!", "?", ";"]:
            time.sleep(random.uniform(0.3, 0.6))
        # Occasionally add an extra pause after a space.
        elif char == " ":
            time.sleep(random.uniform(0.1, 0.3))

    # Simulate pressing Enter at the end of the message.
    keyboard.press_and_release("enter")
    print(f"Typed message: {message}")


def on_shortcut() -> None:
    """
    Callback function triggered by the hotkey to type the next message.
    """
    global message_index
    if message_index < len(MESSAGES):
        type_message(MESSAGES[message_index])
        message_index += 1
    else:
        print("All messages have been sent.")


def main() -> None:
    # Use "ctrl+shift+1" as the hotkey; this combination is generally safe in browsers.
    shortcut = "ctrl+shift+1"
    print(f"Press {shortcut} to type the next message. Press ESC to exit.")

    # Register the hotkey.
    keyboard.add_hotkey(shortcut, on_shortcut)

    # Keep the script running until the user presses the ESC key.
    keyboard.wait("esc")
    print("Exiting...")


if __name__ == "__main__":
    main()
