from PIL import Image
import pytesseract

# If you don't have tesseract executable in your PATH, include the following:
# pytesseract.pytesseract.tesseract_cmd = r'~/.virtualenvs/playground/bin/pytesseract'
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

# Simple image to string
s = pytesseract.image_to_string(Image.open('readthis.png'))

print(s)