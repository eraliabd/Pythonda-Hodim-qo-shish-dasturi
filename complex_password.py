"""
Muallif: Abdinazarov Erali
Sana: 14-01-2022
Murakkab parol yaratish
"""
import random as r

belgilar = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+=-'
parol=""
for i in range(16):
    son = r.randint(0,len(belgilar)-1)
    parol+=belgilar[son]
print(parol)