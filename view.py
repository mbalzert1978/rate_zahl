class ViewRateZahl:
    @staticmethod
    def print_Banner() -> None:
        print("RateSpiel 1.0")
        print("Gib eine Zahl zwischen 0 und 10 an um zu raten.")

    @staticmethod
    def print_rate_zahl_eingabe_fehler():
        print("Bitte geben Sie eine Zahl zwischen 0 und 10 an")

    @staticmethod
    def print_rate_zahl_falsch_geraten():
        print("Leider Falsch geraten! Du verlierst ein Leben")

    @staticmethod
    def print_gewonnen(zahl: int):
        print("Game Over")
        print("Richtig geraten!")
        print(f"Die gesuchte Zahl war: {zahl}")

    @staticmethod
    def print_tip(ist_kleiner: bool):
        if not ist_kleiner:
            print("Deine gewählte Zahl ist zu groß")
            return
        print("Deine gewählte Zahl ist zu klein")

    @staticmethod
    def spiel_zu_ende_verlore(zahl: int):
        print("Game Over")
        print(f"Die gesuchte Zahl war: {zahl}")
