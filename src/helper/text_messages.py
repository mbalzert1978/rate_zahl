from enum import Enum


class RateZahlMessages(Enum):
    DISPLAY_TITLE = (
        "RateSpiel 1.0\n"
        + "Erate eine zufällige Zahl mit 3 Leben. Viel Spaß\n"
        + "#" * 20
    )
    DISPLAY_FOOTER = "#" * 20
    DISPLAY_GAMEOVER = "Game Over\nDie gesuchte Zahl wahr: "
    DISPLAY_GAMEOVER_WON = (
        "Game Over\n"
        + "Du hast gewonnen\n"
        + "Du hast die gesuchte Zahl gefunden."
    )
    DISPLAY_LIFE_LOST = "Leider Falsch geraten! Du verlierst ein Leben"
    HINT_BIG = "Deine gewählte Zahl ist zu groß"
    HINT_SMALL = "Deine gewählte Zahl ist zu klein"
