import subprocess

import pytesseract
from PIL import Image

image = Image.open("num.png")
image = image.point(lambda x: 0 if x < 196 else 255)
image.save("newNum.png")
image.show()

newImage = Image.open("newNum.png")

text = pytesseract.image_to_string(newImage, lang="eng")
print(text)