import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=20,
    border=2
)

qr.add_data('checkpoint_A')
qr.make(fit=True)

img = qr.make_image(fill_color='black', back_color='white')
img.save('checkpoint_A.png')

"""  """

qr_b = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=20,
    border=2
)

qr_b.add_data('checkpoint_B')
qr_b.make(fit=True)

img_b = qr_b.make_image(fill_color='black', back_color='white')
img_b.save('checkpoint_B.png')