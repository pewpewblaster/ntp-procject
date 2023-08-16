import winreg

# path to the NTP application settings in the winreg
# saved Computer\HKEY_CURRENT_USER\Software\ntp_aplikacija
key_path = r"Software\ntp_aplikacija"
    
def win_reg_app_data():
    values_dict = {}
    
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_READ)
        index = 0
        while True:
            try:
                value_name, value_data, value_type = winreg.EnumValue(key, index)
                if value_type == winreg.REG_SZ:
                    values_dict[value_name] = value_data
                index += 1
            except OSError:
                break
        winreg.CloseKey(key)
        return values_dict
    
    except FileNotFoundError:
        print("Registry key not found.")