from PyQt6.QtGui import QGuiApplication, QFontDatabase
import sys

# Create a QGuiApplication instance
app = QGuiApplication(sys.argv)

# Initialize the font database
font_db = QFontDatabase()

# Get a list of available font families for the Latin writing system
writing_system = QFontDatabase.WritingSystem.Latin
font_families = font_db.families(writing_system)

# Print the list of fonts
for font_family in font_families:
    print(font_family)
