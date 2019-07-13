import pytesseract
from PIL import Image

def ocr_core(filename):  
    img = Image.open(filename)
    img = img.convert('L')
    img.save(filename)

    text = pytesseract.image_to_string(Image.open(filename))  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text

print(ocr_core('Images/image2.jpg'))