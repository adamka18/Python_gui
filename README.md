# GUI Számológép Projekt

Készítette: 1. Csapat (Kevin, Anasztázia, Ádám, Vivien, István)  
Dokumentáció: Balog István

---

## 📌 Projekt leírás
Ez a projekt egy modern, grafikus felhasználói felülettel (GUI) rendelkező számológép alkalmazás, amely Python nyelven készült.  
A program célja az alapvető matematikai műveletek egyszerű és felhasználóbarát elvégzése, valamint a programozási alapelvek (modularitás, tesztelés, hibakezelés) bemutatása.

---

## ⚙️ Funkciók
- Alapvető matematikai műveletek (+, -, *, /)
- Haladó műveletek (hatványozás, négyzetgyök)
- Grafikus felhasználói felület (GUI, dark mode)
- Előzmények kezelése
- Hibakezelés:
  - Nullával való osztás
  - Hibás bemenetek kezelése
- Egységtesztek (pytest)

---

## 🏗️ Projekt felépítése
projekt/
│── main.py # GUI (felhasználói felület)
│── logic.py # Számítási logika
│── test_logic.py # Tesztek
│── README.md # Dokumentáció


---

## 🧠 Működési elv

A projekt rétegekre van bontva:

- **logic.py**
  - A számításokat végzi
  - Kivételeket dob hibák esetén

- **main.py**
  - Kezeli a felhasználói felületet
  - Megjeleníti az eredményeket
  - Kezeli a hibákat

- **test_logic.py**
  - Automatikus teszteket tartalmaz
  - Ellenőrzi a program helyes működését

---

## 🚀 Használat

1. Telepítsd a Pythont
2. (Opcionális) Telepítsd a szükséges csomagokat:
python -m pip install ttkbootstrap pytest

3. Indítás:

python main.py

---

## 🧪 Tesztelés

A tesztek futtatása:
python -m pytest


Várt eredmény:

X passed

---

## 🎯 Cél

A projekt célja:
- a Python GUI fejlesztés bemutatása
- a tiszta kód és moduláris felépítés alkalmazása
- az automatizált tesztelés alapjainak megismerése

---

## 👥 Készítők

- Szántó Kevin (GUI)
- Szenykó Anasztázia (GUI)
- Temető Ádám (logika, projektvezető)
- Tóth Vivien (tesztelés)
- Balog István (dokumentáció)
