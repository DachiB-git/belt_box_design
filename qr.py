import qrcode
img = qrcode.make("https://wa.me/c/995598717455")
type(img)  # qrcode.image.pil.PilImage
img.save("qr.png")