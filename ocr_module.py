import pytesseract
from PIL import Image

# Optional: Set Tesseract path if not in PATH (e.g., on Windows)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_image(image_path):
    """
    Extracts text from an image using Tesseract OCR.
    Handles handwritten-style prescriptions.
    """
    img = Image.open(image_path)
    # Use English as default lang for medical prescriptions; adjust if needed
    text = pytesseract.image_to_string(img, lang='eng')
    return text.strip()