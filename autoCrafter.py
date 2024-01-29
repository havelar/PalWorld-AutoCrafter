import keyboard

HEADER = '''
Holds F to Auto-Craft in PalWorld.

F12 -> To start holding F
W A S D F -> To stop holding F
Pause / Break -> To close the program
'''

class PalWorld:
    running: bool = False

    @classmethod
    def AutoCraft(cls, kb_evt: keyboard.KeyboardEvent) -> None:
        if cls.running is False and kb_evt.scan_code == 88: # F12
            cls.running=True
            print(f'[{kb_evt.name.upper()}] - Começando')
            keyboard.press("f")
    
        if cls.running is True and kb_evt.scan_code in (17, 30, 31, 32, 33, 69): # w, a, s, d, f, pause/break
            cls.running = False
            print(f'[{kb_evt.name.upper()}] - Parando')
            keyboard.release("f")

if __name__ == "__main__":
    print(HEADER)
    keyboard.hook(PalWorld.AutoCraft)
    keyboard.wait(hotkey=69, trigger_on_release=True, suppress=True)
