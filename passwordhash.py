from pwdlib import PasswordHash
password_has=PasswordHash.recommended()
password="12345"
hashed=password_has.hash(password)
print("hashed password",hashed)
print("the real password will be",password)
if password_has.verify(password,hashed):
    print("login sucessfull")
else:
    print("not valid")