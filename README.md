# MacWiFiConnect

MacWiFiConnect is a Python script designed to automate the process of connecting to a Wi-Fi network on macOS using a list of potential passwords. This can be particularly useful for network administrators or users who need to try multiple passwords to connect to a Wi-Fi network.

## Features

- Connect to a specified Wi-Fi network using a list of passwords.
- Check and verify the connection status.
- Read passwords from a file.

## Requirements

- macOS
- Python 3.x

## Installation

1. Clone the repository or download the script file.
2. Ensure you have Python 3.x installed on your macOS system.

## Usage

1. Prepare a text file containing a list of possible passwords, with one password per line.
2. Open the script and modify the `ssid` variable to your Wi-Fi network's SSID.
3. Modify the `password_file_path` variable to the path of your password file.
4. Run the script:

```bash
python3 macwifi_connect.py
```
## Example

```python
ssid = "example ssid"  # Replace with your SSID
password_file_path = "./pass.txt"  # Replace with the path to your password file
```
## Disclaimer
MacWiFiConnect is intended for legal and authorized use only.

The author of this script are not responsible for any misuse of this script. This script should not be used to gain unauthorized access to any Wi-Fi network. Unauthorized access to computer networks is illegal and punishable by law. Use this script responsibly and only on networks you have permission to access.

## License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/egwyl666/MacWiFiConnect?tab=MIT-1-ov-file) file for details.
