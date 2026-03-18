"""
A számológép grafikus felületét (GUI) megvalósító modul.

Ez a modul felelős:
- a felhasználói felület megjelenítéséért (ttkbootstrap segítségével, sötét témában)
- a felhasználói input kezeléséért (gombok)
- a számítások delegálásáért a logikai rétegnek (logic.py)
- az előzmények tárolásáért és megjelenítéséért
- az alapvető hibakezelésért

Felépítés:
- logic.py → számítási logika (kivételt dob hibák esetén)
- main.py → GUI és felhasználói interakció

Készítette:
- Szántó Kevin
- Szenykó Anasztázia
"""

import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from logic import calculate


class CalculatorApp:
    def __init__(self, root):
        # Főablak inicializálása
        self.root = root
        self.root.title("Számológép GUI")
        self.root.geometry("350x500")
        self.root.resizable(False, False)

        # Számítási előzmények tárolása
        self.history = []

        self.create_widgets()

    def create_widgets(self):
        # Beviteli mező (kijelző)
        self.entry = ttk.Entry(
            self.root,
            font=("Segoe UI", 20),
            justify="right",
            bootstyle="dark"
        )
        self.entry.pack(fill="x", padx=10, pady=15)

        # Gombok konténere
        frame = ttk.Frame(self.root)
        frame.pack(expand=True, fill="both", padx=10, pady=10)

        # Gombkiosztás
        buttons = [
            ('7','8','9','/'),
            ('4','5','6','*'),
            ('1','2','3','-'),
            ('0','.','=','+'),
            ('C','^','√','H')
        ]

        # Gombok létrehozása dinamikusan
        for r, row in enumerate(buttons):
            for c, char in enumerate(row):
                style = "secondary"

                # Stílus beállítása funkció szerint
                if char == "=":
                    style = "success"
                elif char in ['+', '-', '*', '/', '^']:
                    style = "info"
                elif char == "C":
                    style = "danger"
                elif char == "H":
                    style = "warning"

                ttk.Button(
                    frame,
                    text=char,
                    bootstyle=style,
                    command=lambda t=char: self.on_click(t)
                ).grid(row=r, column=c, sticky="nsew", padx=5, pady=5)

        # Reszponzív elrendezés
        for i in range(5):
            frame.rowconfigure(i, weight=1)
        for i in range(4):
            frame.columnconfigure(i, weight=1)

    def on_click(self, char):
        """
        Gombkattintások kezelése.
        A lenyomott gomb alapján különböző műveleteket hajt végre.
        """
        if char == "C":
            # Kijelző törlése
            self.entry.delete(0, END)

        elif char == "=":
            # Számítás végrehajtása
            self.calculate()

        elif char == "H":
            # Előzmények megjelenítése
            self.show_history()

        elif char == "√":
            # Négyzetgyök számítása (egy operandus)
            try:
                num = float(self.entry.get())
                result = calculate(num, None, '√')
                self.entry.delete(0, END)
                self.entry.insert(0, result)
                self.history.append(f"√{num} = {result}")
            except Exception:
                self.entry.insert(0, "Hiba")

        else:
            # Karakter hozzáfűzése a kijelzőhöz
            self.entry.insert(END, char)

    def calculate(self):
        """
        A bevitt kifejezés feldolgozása és kiszámítása.
        Az alap műveleteket támogatja (+, -, *, /, ^).
        """
        try:
            expr = self.entry.get()

            # Operátor felismerése és a kifejezés felbontása
            for op in ['+', '-', '*', '/', '^']:
                if op in expr:
                    n1, n2 = expr.split(op)
                    result = calculate(float(n1), float(n2), op)

                    # Eredmény mentése az előzményekbe
                    self.history.append(f"{expr} = {result}")

                    # Eredmény megjelenítése
                    self.entry.delete(0, END)
                    self.entry.insert(0, result)
                    return

        except Exception:
            self.entry.insert(0, "Hiba")

    def show_history(self):
        """
        Új ablakban megjeleníti az eddigi számítások előzményeit.
        """
        win = ttk.Toplevel(self.root)
        win.title("Előzmények")

        text = ttk.Text(win, height=15)
        text.pack(fill="both", expand=True, padx=10, pady=10)

        for item in self.history:
            text.insert(END, item + "\n")


# Program belépési pont
if __name__ == "__main__":
    root = ttk.Window(themename="darkly")
    app = CalculatorApp(root)
    root.mainloop()