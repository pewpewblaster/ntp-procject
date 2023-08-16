import winreg

# Define the registry key path
key_path = r"Software\ntp_aplikacija"

# Open the registry key
try:
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_READ)
    print(f"Strings and their values under '{key_path}':")
    index = 0
    while True:
        try:
            value_name, value_data, value_type = winreg.EnumValue(key, index)
            if value_type == winreg.REG_SZ:
                print(f"{value_name}: {value_data}")
            index += 1
        except OSError:
            break
    winreg.CloseKey(key)
except FileNotFoundError:
    print("Registry key not found.")
