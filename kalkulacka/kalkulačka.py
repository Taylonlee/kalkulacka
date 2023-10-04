class Kalkulacka:
    """Reprezentuje Kalkulačku, která slouží pro výpočet dvou čísel."""
    def main(self):
        while True:
            try:
                self.prvni_cislo = float(input("Zadej 1. číslo: \n"))
                break
            except ValueError:
                print("Zadej prosím číslo!")
        while True:
            try:
                self.druhe_cislo = float(input("Zadej 2. číslo: \n"))
                break
            except ValueError:
                print("Zadej prosím číslo!")

    def scitani(self):
        """Funkce pro sčítání dvou čísel."""
        return f"Součet: {self.prvni_cislo + self.druhe_cislo}"

    def odecitani(self):
        """Funkce pro odečítání dvou čísel."""
        return f"Rozdíl: {self.prvni_cislo - self.druhe_cislo}"

    def nasobeni(self):
        """Funkce pro násobení dvou čísel."""
        return f"Součin: {self.prvni_cislo * self.druhe_cislo}"

    def deleni(self):
        """Funkce pro dělení dvou čísel."""
        try:
            return f"Podíl: {self.prvni_cislo / self.druhe_cislo}"
        except ZeroDivisionError:
            print("Nulou nelze dělit!")