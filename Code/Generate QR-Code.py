import qrcode
from PIL import Image

QR= qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

QR.add_data("https://www.inc.com/peter-economy/11-elon-musk-quotes-that-will-push-you-to-achieve-impossible.html")
QR.make(fit=True)

img = QR.make_image(fill_color="black", back_color="white")
img.save("qrcode.png")
