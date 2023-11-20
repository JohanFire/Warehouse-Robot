import qrcode

qr = qrcode.make('checkpoint_A')
qr.save('checkpoint_A.png')

qr_b = qrcode.make('checkpoint_B')
qr_b.save('checkpoint_B.png')