import nltk
from nltk.corpus import words
from difflib import get_close_matches
from pynput import keyboard
import pyperclip
from AppKit import NSApplication, NSApp, NSStatusBar, NSMenu, NSMenuItem, NSObject, NSAlert, NSRunningApplication, NSApplicationActivateIgnoringOtherApps, NSVariableStatusItemLength

# Ensure the word list is downloaded
nltk.download('words')
word_list = words.words()

def find_closest_word(target):
    matches = get_close_matches(target, word_list, n=1)
    return matches[0] if matches else target

def get_current_word():
    # Placeholder function: You need to replace this with actual text editor interaction
    pyperclip.copy('sample_word')  # Example word
    return pyperclip.paste()

def replace_word(old_word, new_word):
    # Placeholder function: You need to replace this with actual text editor interaction
    print(f'Replacing "{old_word}" with "{new_word}"')

class KeyHandler:
    def __init__(self):
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()

    def on_press(self, key):
        try:
            if key == keyboard.Key.alt and keyboard.Controller().press(keyboard.Key.delete):
                current_word = get_current_word()
                closest_word = find_closest_word(current_word)
                replace_word(current_word, closest_word)
        except AttributeError:
            pass

class AppDelegate(NSObject):
    def applicationDidFinishLaunching_(self, notification):
        self.statusBar = NSStatusBar.systemStatusBar()
        self.statusItem = self.statusBar.statusItemWithLength_(NSVariableStatusItemLength)
        self.statusItem.setTitle_("WordReplacer")
        self.statusItem.setHighlightMode_(1)
        self.statusMenu = NSMenu.alloc().init()

        menuItem = NSMenuItem.alloc().initWithTitle_action_keyEquivalent_("Quit", "terminate:", "")
        self.statusMenu.addItem_(menuItem)

        self.statusItem.setMenu_(self.statusMenu)

def main():
    app = NSApplication.sharedApplication()
    delegate = AppDelegate.alloc().init()
    app.setDelegate_(delegate)

    # Activate the application
    NSRunningApplication.currentApplication().activateWithOptions_(NSApplicationActivateIgnoringOtherApps)

    key_handler = KeyHandler()

    NSApp.run()

if __name__ == "__main__":
    main()
