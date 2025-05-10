# File/Folder Hide/Unhide Script

This Python script allows users to hide and un-hide specific files or folders by toggling their system attributes, based on a password.

## Features

- Hides files or folders by adding hidden and system attributes.
- Un-hides files or folders by removing hidden and system attributes.
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
   item_you_want_to_hide: Path = Path("C:\\path\\to\\your\\file_or_folder")
   ```

2. **Set your password:**

   Type your password between the single quotes:

   ```python
   password: str = 'yourpassword'
   ```

3. **Add more items (optional):**

   If you have multiple items (files and/or folders) to hide/un-hide, enter their variable names in the `items` list. For example:

   ```python
   items: list[Path] = [item_you_want_to_hide, item_you_want_to_hide, item_you_want_to_hide]
   ```

4. **Run the script:**

   Execute the script and if your files and folders are already hidden then entering the password will un-hide them, if they are visible then the password will hide them.


## Notes

- This script works for **both files and folders** on **Windows**.
- Be careful when hiding system files or important folders as they can become inaccessible or hidden from the file explorer.

## License

This project is licensed under the MIT License.
