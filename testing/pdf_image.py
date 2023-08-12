import pyodbc
import PIL.Image as Image
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Image, Spacer
import os
from datetime import datetime

# Povezivanje s bazom podataka
conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=db/skladiste.accdb;')
cursor = conn.cursor()

# Dohvati podatke iz tablice "proizvodi"
cursor.execute('SELECT privitak FROM proizvodi WHERE privitak IS NOT NULL')
rows = cursor.fetchall()

# Create a PDF document
pdf_buffer = BytesIO()
doc = SimpleDocTemplate(pdf_buffer, pagesize=letter)

# Create a list to hold your flowables (content)
elements = []

# Iteriraj kroz redove i obradi slike
for row in rows:
    img_data = row.privitak
    img_stream = BytesIO(img_data)
    img = Image(img_stream)

    # Get the dimensions of the image
    img_width = img.drawWidth
    img_height = img.drawHeight

    # Resize the image to fit within the available space
    max_width = 456.0  # Maximum width of the frame
    max_height = 636.0  # Maximum height of the frame

    if img_width > max_width or img_height > max_height:
        img_width_ratio = max_width / img_width
        img_height_ratio = max_height / img_height
        img_ratio = min(img_width_ratio, img_height_ratio)
        img_width *= img_ratio
        img_height *= img_ratio

    # Add the image to the list of elements
    img.drawWidth = img_width
    img.drawHeight = img_height
    elements.append(img)
    elements.append(Spacer(1, 10))  # Add some space between images
    
# Build the PDF document
doc.build(elements)

# Generate a timestamp-based filename
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
pdf_filename = f'reports/images_pdf/{timestamp}.pdf'

# Save the PDF to the specified path
with open(pdf_filename, 'wb') as pdf_file:
    pdf_file.write(pdf_buffer.getvalue())

print('PDF slike su spremljene u', pdf_filename)