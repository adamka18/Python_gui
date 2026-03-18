"""
A számológép logikai rétegét megvalósító modul.

Ez a modul felelős a matematikai műveletek végrehajtásáért.
A `calculate` függvény különböző operátorok alapján végzi el a számításokat.

Támogatott műveletek:
- Összeadás (+)
- Kivonás (-)
- Szorzás (*)
- Osztás (/)
- Hatványozás (^)
- Négyzetgyök (√)

Hibakezelés:
- Nullával való osztás esetén ZeroDivisionError kivételt dob
- Ismeretlen operátor esetén ValueError kivételt dob

Tervezési elv:
A függvény nem kezeli le a hibákat (nem try-except), hanem kivételt dob,
így a hívó réteg (pl. GUI) felelőssége a hibák kezelése.

Készítette:
- Temető Ádám
"""

import math

def calculate(num1, num2, operator):
    if operator == '+': return num1 + num2
    if operator == '-': return num1 - num2
    if operator == '*': return num1 * num2
    if operator == '/':
        if num2 == 0:
            raise ZeroDivisionError("Nullával nem lehet osztani")
        return num1 / num2
    if operator == '^': return num1 ** num2
    if operator == '√': return math.sqrt(num1)

    raise ValueError("Ismeretlen művelet")