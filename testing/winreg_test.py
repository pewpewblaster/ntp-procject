import winreg

# Open the registry key
key_path = r"Software\ntp_aplikacija"
key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE)

# Get the values from setGeometry
x, y, width, height = 100, 100, 250, 300
geometry_value = f"{x},{y},{width},{height}"

# Save the geometry value in the registry key
winreg.SetValueEx(key, "geometry", 0, winreg.REG_SZ, geometry_value)

# Close the registry key
winreg.CloseKey(key)
