"""Hides and un-hides a folder based on a entered password"""

import os
from pathlib import Path
import ctypes
import time

FILE_ATTRIBUTE_HIDDEN: int = 0X02
FILE_ATTRIBUTE_SYSTEM: int = 0X04
hidden_items = None
visible_items = None
# Change variable name and enter the path to specific
# directory/file betweeen the quotes
# Add more if you have more than one directory or file
item_you_want_to_hide: str = Path("")
# Within the quotes change the place holder password with your own
password: str = "placeholderpassword"

# Enter the names of the above variables and
# seperate with ', ' (folder1, file1, folder2)
items = ()


def hide_item(item: str) -> None:
    """Hides specified item by changing its attributes"""

    if os.path.exists(item):
        os.system(f'attrib +h +s "{item}"')

    else:
        pass


def un_hide_item(item: str) -> None:
    """Un-hides specified item by changing its attributes"""

    if os.path.exists(item):
        os.system(f'attrib -h -s "{item}"')

    else:
        pass


def item_attribute_reset(items: tuple) -> None:
    """Reset all files attributes to hidden"""

    for item in items:
        hide_item(item)


def check_item_attributes(items: tuple) -> None:
    """Check the attributes for the folder"""

    global hidden_items
    global visible_items

    num_hidden_items: int = 0
    num_visible_items: int = 0
    for item in items:
        item_path_str = str(item)
        item_path_wide: ctypes.c_wchar_p = ctypes.c_wchar_p(item_path_str)
        attrs: int = ctypes.windll.kernel32.GetFileAttributesW(item_path_wide)

        if attrs == -1:
            continue

        elif attrs & FILE_ATTRIBUTE_HIDDEN or attrs & FILE_ATTRIBUTE_SYSTEM:
            num_hidden_items += 1

        elif (not attrs & FILE_ATTRIBUTE_HIDDEN or
              attrs & FILE_ATTRIBUTE_SYSTEM):

            num_visible_items += 1

    if isinstance(num_hidden_items, int):
        if num_hidden_items == 0:
            hidden_items = False

        elif num_hidden_items > 0:
            hidden_items = True

    if isinstance(num_visible_items, int):
        if num_visible_items == 0:
            visible_items = False

        elif num_visible_items > 0:
            visible_items = True

    else:
        item_attribute_reset(items)


check_item_attributes(items)

if hidden_items is True and visible_items is True:
    item_attribute_reset(items)

check_item_attributes(items)

print("\nWelcome to the file backup script! Please enter the backup "
      "sequence code as per manual!\n")
print("This will backup all files, please proceed with caution!!\n")
print("Enter 'q' to exit\n\n")

while True:
    user_input: str = input("Sequence Code: ")

    if user_input.strip() == password:

        if hidden_items is True and visible_items is False:
            for item in items:
                un_hide_item(item)
            print("\nSequance code accepted!\n")
            time.sleep(1)
            break

        elif hidden_items is False and visible_items is True:
            for item in items:
                hide_item(item)
            print("\nSequance code accepted!\n")
            time.sleep(1)
            break

    elif user_input == 'q'.strip().lower():
        break

    else:
        print("\nInvalid Sequance Code! Aborting Backup!\n")
        time.sleep(1)
        break
