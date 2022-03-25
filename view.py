class ViewRateZahl:
    @staticmethod
    def rate_zahl_header() -> None:
        print("RateSpiel 1.0")
        print("Erate eine zufällige Zahl mit 3 Leben. Viel Spaß")
        print("#" * 20)

    @staticmethod
    def rate_zahl_footer() -> None:
        print("#" * 20)

    @staticmethod
    def rate_zahl_eingabe_fehler():
        print("Bitte geben Sie eine Zahl zwischen 0 und 10 an")

    @staticmethod
    def rate_zahl_falsch_geraten():
        print("Leider Falsch geraten! Du verlierst ein Leben")

    @staticmethod
    def rate_zahl_gewonnen(zahl: int):
        print("Game Over")
        print("Richtig geraten!")
        print(f"Die gesuchte Zahl war: {zahl}")

    @staticmethod
    def rate_zahl_tip(ist_kleiner: bool):
        if not ist_kleiner:
            print("Deine gewählte Zahl ist zu groß")
            return
        print("Deine gewählte Zahl ist zu klein")

    @staticmethod
    def rate_zahl_zu_ende_verlore(zahl: int):
        print("Game Over")
        print(f"Die gesuchte Zahl war: {zahl}")
