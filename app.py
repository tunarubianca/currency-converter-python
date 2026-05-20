import requests
class Moneda:
    def __init__(self, cod, rata):
        self.cod = cod
        self.rata = rata 

    def converteste_in(self, suma, obiect_moneda_tinta):
        rezultat = (suma / self.rata) * obiect_moneda_tinta.rata
        return round(rezultat, 2)

class Euro(Moneda):
    def __init__(self):
        super().__init__("EUR", 1.0)

class Dolar(Moneda):
    def __init__(self, rata):
        super().__init__("USD", rata)

class Leu(Moneda):
    def __init__(self, rata):
        super().__init__("RON", rata)


print("--- CONVERTORUL PORNEȘTE ACUM ---")

try:
    # Încercăm API-ul, dacă nu merge, punem valori fixe
    data = requests.get("https://www.floatrates.com/daily/eur.json", timeout=2).json()
    usd_val = data["usd"]["rate"]
    ron_val = data["ron"]["rate"]
except:
    usd_val, ron_val = 1.08, 4.97

# Creăm obiectele
monede = {
    "EUR": Euro(),
    "USD": Dolar(usd_val),
    "RON": Leu(ron_val)
}


try:
    suma = float(input("Introdu suma (număr): "))
    sursa = input("Din ce monedă (EUR/USD/RON): ").upper()
    tinta = input("În ce monedă (EUR/USD/RON): ").upper()

    if sursa in monede and tinta in monede:
        ob_sursa = monede[sursa]
        ob_tinta = monede[tinta]
        
        # Obiectul sursă comunică cu obiectul țintă
        rezultat = ob_sursa.converteste_in(suma, ob_tinta)
        print(f"\nREZULTAT: {suma} {sursa} = {rezultat} {tinta}")
    else:
        print("Eroare: Monedă inexistentă.")
except ValueError:
    print("Eroare: Trebuie să introduci un număr pentru sumă!")

input("\nProgramul s-a terminat. Apasă ENTER ")
