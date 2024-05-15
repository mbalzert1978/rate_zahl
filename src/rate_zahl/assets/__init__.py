from src.rate_zahl.model.enums import GameState, Hint

GAMETEXT: dict[str, str] = {
    GameState.GUESSED: ("Guess a number between 1 and 100: "),
    GameState.NUMBER: ("Enter a number between 1 and 100!"),
    Hint.BIG: ("You guessed to big."),
    Hint.SMALL: ("You guessed to small."),
    GameState.WON: ("Won you guessed correctly.", "You win."),
    GameState.GAME_OVER: ("Game over.", "You lost.", "The number was {value}"),
}
