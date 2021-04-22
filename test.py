import qrcode
img = qrcode.make('https://latifyilmaz.com')
img.save("qrcode.png");

print(img)