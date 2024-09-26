# File/Folder Hide/Unhide Script

This Python script allows users to hide and un-hide specific files or folders by toggling their system attributes, based on a password.

## Features

- Hides specified files or folders by adding system and hidden attributes.
- Un-hides files or folders by removing system and hidden attributes.
- Uses a password for authentication.
- Supports multiple files or folders at once.
- Can reset item attributes automatically.

## Requirements

- Python 3.x
- Windows OS (as it uses the `attrib` and `kernel32` Windows API)

## Usage

1. **Set the items to hide/un-hide:**

   In the script, specify the path to the files or folders you want to hide by setting the `item_you_want_to_hide` variable. For example:

   ```python
   item_you_want_to_hide: str = Path("C:\\path\\to\\your\\file_or_folder")
   ```

2. **Set your password:**

   Replace the placeholder password in the `password` variable with your own password:

   ```python
   password: str = "yourpassword"
   ```

3. **Add more items (optional):**

   If you have multiple items (files and/or folders) to hide/un-hide, enter their variable names in the `items` tuple. For example:

   ```python
   items = (item_you_want_to_hide, item_you_want_to_hide, item_you_want_to_hide)
   ```

4. **Run the script:**

   Execute the script in a terminal/command prompt and enter the correct password to hide/un-hide the specified items. The script will toggle the visibility of each file or folder based on their current attributes.

   ```bash
   python hide_unhide.py
   ```

5. **Exit the script:**

   You can exit the script at any time by entering `q`.

## Functions

- **`hide_item(item: str) -> None`**: Hides the specified file or folder by setting the hidden and system attributes.
- **`un_hide_item(item: str) -> None`**: Un-hides the specified file or folder by removing the hidden and system attributes.
- **`check_item_attributes(item: str) -> None`**: Checks the attributes of the files or folders to determine their visibility status.
- **`item_attribute_reset(items: tuple) -> None`**: Resets the attributes of all specified files or folders to be hidden.

## Notes

- This script works for **both files and folders** on **Windows**.
- Be careful when hiding system files or important folders as they can become inaccessible or hidden from the file explorer.

## License

This project is licensed under the MIT License.
