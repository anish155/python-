import qrcode

data="https://www.google.com/"

qr=qrcode.make(data)

qr.save("qr.png")
