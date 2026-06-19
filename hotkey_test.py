import keyboard

keyboard.add_hotkey("Shift+q", lambda: print("SHIFT Q was pressed"))
keyboard.add_hotkey("Shift+x", lambda: print("SHIFT  X was pressed"))
keyboard.wait()
