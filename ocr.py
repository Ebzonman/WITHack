import pytesseract
import pyocr
import pyocr.builders
# import cv2 
# import numpy as np
from PIL import Image

def ocrpy(filename):
    tools = pyocr.get_available_tools()[0]
    text = tools.image_to_string(Image.open(filename), builder=pyocr.builders.TextBuilder())

def tessocr(filename):  
    img = Image.open(filename)
    img = img.convert('L')
    img.save(filename)

    text = pytesseract.image_to_string(Image.open(filename))  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text

# print(pyocr_core('Images/image4.jpeg'))