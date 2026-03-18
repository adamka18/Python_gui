"""
A számológép logikai rétegének tesztelését megvalósító modul.

Ez a modul a `calculate` függvény helyes működését ellenőrzi különböző
bemenetek és esetek alapján. A tesztek célja, hogy biztosítsák a program
megbízható működését és a hibák megfelelő kezelését.

Tesztelt területek:
- Alap műveletek (összeadás, kivonás, szorzás, osztás)
- Speciális műveletek (hatványozás, négyzetgyök)
- Hibakezelés (nullával való osztás, negatív gyök, érvénytelen operátor)
- Több bemeneti kombináció tesztelése parametrizált módon

Hibakezelés tesztelése:
- pytest.raises használata a kivételek ellenőrzésére
- biztosítja, hogy a program megfelelő hibát dobjon hibás input esetén

Tervezési elv:
A tesztek lefedik a legfontosabb működési eseteket (happy path + edge case),
így segítik a stabil és karbantartható kód fejlesztését.

Készítette:
- Tóth Vivien
"""

import pytest
from logic import calculate

def test_addition():
    assert calculate(10, 5, '+') == 15

def test_subtraction():
    assert calculate(10, 5, '-') == 5

def test_multiplication():
    assert calculate(4, 3, '*') == 12

def test_division():
    assert calculate(10, 2, '/') == 5


def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculate(10, 0, '/')


def test_power():
    assert calculate(2, 3, '^') == 8


def test_square_root():
    assert calculate(9, None, '√') == 3


def test_square_root_negative():
    with pytest.raises(ValueError):
        calculate(-9, None, '√')


def test_invalid_operator():
    with pytest.raises(ValueError):
        calculate(10, 5, '%')


@pytest.mark.parametrize("a,b,op,expected", [
    (1, 1, '+', 2),
    (5, 3, '-', 2),
    (2, 4, '*', 8),
    (8, 2, '/', 4),
])
def test_multiple_operations(a, b, op, expected):
    assert calculate(a, b, op) == expected