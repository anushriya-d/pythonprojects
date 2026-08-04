import qrcode

website_link = "https://github.com/anushriya-d"

qr = qrcode.QRCode(version = 1, box_size = 6, border = 6)

qr.add_data(website_link)
qr.make()

img = qr.make_image(fill_color = '#C71585', back_color = 'white')

img.save('github_qr.png')