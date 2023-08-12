from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_pdf(file_name):
    c = canvas.Canvas(file_name, pagesize=letter)
    c.drawString(100, 750, "Dobrodošli u generiranje PDF-a pomoću Pythona!")
    c.save()

if __name__ == "__main__":
    generate_pdf("primjer.pdf")