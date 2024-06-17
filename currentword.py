import os
from AppKit import NSWorkspace
from Quartz import (
    AXUIElementCopyAttributeValue,
    AXUIElementCreateSystemWide,
    kAXFocusedUIElementAttribute,
    kAXValueAttribute,
    kAXSelectedTextAttribute,
    kAXSelectedTextRangeAttribute,
)

def get_current_application():
    workspace = NSWorkspace.sharedWorkspace()
    active_app = workspace.activeApplication()
    return active_app["NSApplicationName"]

def get_focused_element():
    system_wide_element = AXUIElementCreateSystemWide()
    focused_element, error = AXUIElementCopyAttributeValue(system_wide_element, kAXFocusedUIElementAttribute, None)
    if error:
        return None
    return focused_element

def get_value_of_element(element):
    value, error = AXUIElementCopyAttributeValue(element, kAXValueAttribute, None)
    if error:
        return None
    return value

def get_selected_text_range(element):
    selected_range, error = AXUIElementCopyAttributeValue(element, kAXSelectedTextRangeAttribute, None)
    if error:
        return None
    return selected_range

def get_current_word():
    focused_element = get_focused_element()
    if not focused_element:
        return None

    value = get_value_of_element(focused_element)
    if not value:
        return None

    selected_range = get_selected_text_range(focused_element)
    if not selected_range:
        return None

    # Assuming the value is a string (editable text)
    text = value
    cursor_position = selected_range.location

    # Find the current word around the cursor
    word_start = max(text.rfind(' ', 0, cursor_position), 0)
    word_end = text.find(' ', cursor_position)
    if word_end == -1:
        word_end = len(text)

    current_word = text[word_start:word_end].strip()
    return current_word

def main():
    current_app = get_current_application()
    print(f"Current active application: {current_app}")

    current_word = get_current_word()
    if current_word:
        print(f"Current word: {current_word}")
    else:
        print("Unable to determine the current word.")

if __name__ == "__main__":
    main()
