import os.path
import pyqrcode
import png
from pyqrcode import QRCode

# Ask for the user to input a website
site = input("Please enter a website address: ")

# Define the path of the file
path = "/Users/samuelteigland/Downloads/computerProgramming/python/"

# Save to path for the html file
sitePath = os.path.join(path, site)

# Create the QR Code
code = pyqrcode.create(sitePath)

# Create and save the SVG File
svg = code.svg(sitePath + '.svg', scale=8)

# Create and save the PNG File
png = code.png(sitePath + '.png', scale=6)
