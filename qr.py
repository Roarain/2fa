import PIL
from PIL import Image
import qrcode
import pyotp
import uuid
import urllib
from urllib.parse import urlencode,unquote

# 生成8位随机码的imageName
# imageName = "{}.png".format(uuid.uuid1().__str__()[:8])
imageName = 'qr.png'
# 生成base32secret码
# base32secret = pyotp.random_base32()
base32secret = '5cic5no3esqhhdabllgmw6nygzyrxc7p'
# 生成基于OTP的6位随机码
totp = pyotp.TOTP(base32secret)
# 生成基于base32secret的oauth地址
otpuri = pyotp.TOTP(base32secret).provisioning_uri("uri@test.com", issuer_name="uriForTest")
# urldecode
otpuri = unquote(otpuri)
print(otpuri)
'''
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(otpuri)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
'''
# 基于uri生成二维码图片
img = qrcode.make(otpuri)
# 保存图片
img.save(imageName)
# open图片
im = Image.open(imageName)
# 显示图片
im.show()