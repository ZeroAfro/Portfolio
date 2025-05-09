"""
Hides files or items by either adding or removing the
hidden and system attribute from them.
"""

import os
from pathlib import Path
import ctypes
import time
from sys import exit

# Used to check whether the files have been hidden or not already.
# DO NOT REMOVE
FILE_ATTRIBUTE_HIDDEN: int = 0x02
FILE_ATTRIBUTE_SYSTEM: int = 0x04

# Flags used for the functions
hidden_items = None
visible_items = None

# Set the path to the file or folder you wish to hide.
# Replace 'path_goes_here' with the actual path between double quotes.
# Replace 'your_item' with a meaningful variable name if needed.

# You can define a file or folder like this:
# another_folder: Path = Path("C:/path/to/another_folder")
# another_file : Path = Path("C:/path/to/another_file.txt")

your_item: Path = Path("")


# Set your password here, place it inside the single quotes
password: str = ''


# Enter the name(s) you set for your items in the brackets below.
# More than one item needs to seperated with a comma and a space.
# Example: items = [your_item, your_item] or items = [your_item]

items: list[Path] = []


def check_empty_paths(items):
    """
    Verifies that none of the item paths are invalid or empty.
    It will notify you that one of them is and then close 3 sceonds later.
    """

    for item in items:
        if not item or item == Path("") or not item.exists():
            print(
                "One of your items has a invalid or is empty. Closing..."
                )
            time.sleep(3)
            exit()


def hide_item(item: str) -> None:
    """
    Hides items by adding both a hidden
    and system flag to the items.
    """
    try:
        if os.path.exists(item):
            os.system(f'attrib +h +s "{item}"')
    except Exception:
        pass


def un_hide_item(item: str) -> None:
    """
    Un-Hides items by removing both the
    hidden and system flag on the items.
    """
    try:
        if os.path.exists(item):
            os.system(f'attrib -h -s "{item}"')
    except Exception:
        pass


def item_attribute_reset(items: tuple) -> None:
    """
    Resets the attributes of the specified items by hiding them
    regardless of their current state.

    It iterates over the provided items and applies the
    'hidden' and 'system' attributes to each item. This function
    ensures that all items are consistently hidden if both
    hidden and visible items are found.
    """
    try:
        for item in items:
            hide_item(item)
    except Exception:
        pass


def check_item_attributes(items: tuple) -> None:
    """
    Checks the attributes of items to determine if they are hidden,
    visible, or have mixed states.

    - If an error occurs while checking attributes, the item is skipped.
    - Items with 'hidden' or 'system' attributes are counted as hidden.
    - Items that are neither attribute, are counted as visible.

    Hidden Items:
        - If none are found, 'hidden_items' is set to False.
        - If one or more are found, 'hidden_items' is set to True.

    Visible Items:
        - If none are found, 'visible_items' is set to False.
        - If one or more are found, 'visible_items' is set to True.

    If both hidden and visible counts are zero, a fallback is triggered
    by calling 'item_attribute_reset' to re-hide the items.
    """

    global hidden_items
    global visible_items

    num_hidden_items: int = 0
    num_visible_items: int = 0

    for item in items:
        item_path_str = str(item)
        item_path_wide: ctypes.c_wchar_p = ctypes.c_wchar_p(item_path_str)
        attrs: int = ctypes.windll.kernel32.GetFileAttributesW(
            item_path_wide
            )

        if attrs == -1:
            continue

        elif (attrs & FILE_ATTRIBUTE_HIDDEN or
                attrs & FILE_ATTRIBUTE_SYSTEM):
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
        # If for some reason a item is caught by the else statement
        # the items will be reset.
        item_attribute_reset(items)


# ================================
# Code Execution Starts Here
# ================================

# Checks to make sure no items have empty paths.
check_empty_paths(items)

# Checks the attributes of your items at script start.
check_item_attributes(items)

# If a combination of hidden and visible items are found it
# resets them to their hidden state and checks them again.
if hidden_items is True and visible_items is True:
    item_attribute_reset(items)
    check_item_attributes(items)
    print("Loading...")
    time.sleep(2)
    os.system('cls')
    time.sleep(.5)

print("\nWelcome to the file backup script! Please enter the backup "
      "sequence code as per manual!\n")
print("This will backup all files, please proceed with caution!!\n")
print("Enter 'q' to exit\n\n")

while True:
    user_input: str = input("Sequence Code: ")

    if user_input.strip() == password:

        # If there was no visible items it will un-hide your items.
        if hidden_items is True and visible_items is False:
            for item in items:
                un_hide_item(item)
            print("\nSequance code accepted!\n")
            time.sleep(1)
            exit()

        # If your items are visible and not hidden then this will hide them.
        elif hidden_items is False and visible_items is True:
            for item in items:
                hide_item(item)
            print("\nSequance code accepted!\n")
            time.sleep(1)
            exit()

    elif user_input == 'q'.strip().lower():
        exit()

    else:
        print("\nInvalid Sequance Code! Aborting Backup!\n")
        time.sleep(1)
        exit()
