import pyotp
# 校验基于相同base32secret码的随机码是否正确
base32secret = '5cic5no3esqhhdabllgmw6nygzyrxc7p'
totp = pyotp.TOTP(base32secret)

code = '345384'
# 当前随机码
serverCode = totp.now()
if code == serverCode:
    print(True)
else:
    print(False)

