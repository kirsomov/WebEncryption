import string


ALPHABET = string.ascii_letters
ALPHABET += ' '
ALPHABET += string.punctuation


SYMBOLS_TO_POSITIONS = {symbol: i for i, symbol in enumerate(ALPHABET)}
