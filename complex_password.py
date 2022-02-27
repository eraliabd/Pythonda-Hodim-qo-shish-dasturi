"""
Muallif: Abdinazarov Erali
Sana: 14-01-2022
Murakkab parol yaratish
"""
import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbol = "!@#$%^&*()_+=-[]{};"

chars = lower+upper+number+symbol
password = ""

for i in range(8):
    num = random.randint(0, len(chars)-1)
    password += chars[num]
print("Password: ",password)
