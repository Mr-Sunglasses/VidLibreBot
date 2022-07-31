# Import QRCode from pyqrcode
import pyqrcode
import png
from pyqrcode import QRCode
import os


def generate_qr(link):
    url = pyqrcode.create(link)

    url.png("myqr.png", scale=6)


def delete_qr():
    if os.path.exists("myqr.png"):
        os.remove("myqr.png")
