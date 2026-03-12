import random
import string

n = int(input("Berapa karakter password yang mau di buat? "))
karakter = string.ascii_letters + string.digits + string.punctuation
password = ""

for i in range(n):
    password += random.choice(karakter)
print('Password Anda : ', password)    

tes apakah cukup strong pakai def
import random
import string

def cek_kekuatan(password):
    lower = any(c.islower() for c in password)
    upper = any(c.isupper() for c in password)
    digits = any(c.isdigit() for c in password)
    symbol = any(c in string.punctuation for c in password)
    panjang = len(password)

    if panjang > 8 and lower and upper and digits and symbol:
        return "Strong"
    elif panjang > 6:
        return "Medium"
    else:
        return "Weak"

n = int(input("Berapa karakter password yang mau di buat? "))
karakter = string.ascii_letters + string.digits + string.punctuation
password = ""

for i in range(n):
    password += random.choice(karakter)
print('Password Anda : ', password)    
kekuatan = cek_kekuatan(password)
print('Kekuatan : ', kekuatan)
