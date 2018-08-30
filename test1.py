import pyotp

base32secret = pyotp.random_base32()
print(base32secret)
totp = pyotp.TOTP(base32secret)
print(totp.now())
print(totp.verify('343574'))

hotp=pyotp.HOTP(base32secret)
print(hotp.at(0))
print(hotp.at(1))
print(hotp.at(2))

otpuri = pyotp.TOTP(base32secret).provisioning_uri("wangxiaoyu@sensoro.com", issuer_name="Test URI")
print(otpuri)