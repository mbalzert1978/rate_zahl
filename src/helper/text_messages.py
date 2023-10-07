from enum import Enum


class RateZahlMessages(Enum):
    TITLE = (
        "RateSpiel 1.0\n"
        "Erate eine zufällige Zahl mit 3 Leben. Viel Spaß\n" + "#" * 20
    )
    FOOTER = "#" * 20
    GAMEOVER = "Game Over\nDie gesuchte Zahl wahr: %s"
    WON = (
        "Game Over\n"
        "Du hast gewonnen\n"
        "Du hast die gesuchte Zahl %s gefunden."
    )
    LOSELIFE = "Leider Falsch geraten! Du verlierst ein Leben"
    TOBIG = "Deine gewählte Zahl ist zu groß"
    TOSMALL = "Deine gewählte Zahl ist zu klein"
    INPUTERR = "Bitte geben Sie eine Zahl zwischen %s und %s an"
