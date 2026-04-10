
import qrcode
from PIL import Image

data = "https://www.tiktok.com/@codingtogether"
logo_path = "/workspaces/My_Stronghold/artoa/tools/omotograph/logo.png"
logo = Image.open("logo.png")

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.
    ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data(data)
qr.make(fit=True)

qr_img = qr.make_image(fill_color="black",
back_color="white").convert("RGB")

logo = Image.open(logo_path)
logo_size = int(qr_img.size[0] * 0.25)
logo = logo.resize((logo_size, logo_size))

pos = (
    (qr_img.size[0] - logo_size) // 2,
    (qr_img.size[1] - logo_size) // 2
)

qr_img.paste(logo, pos, mask=logo
             if logo.mode == "RGBA" else None)
qr_img.show()
qr_img.save("qr_with_logo.png")

