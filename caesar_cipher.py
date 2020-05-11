import pickle
import string
import math
from alphabet import ALPHABET
from alphabet import SYMBOLS_TO_POSITIONS
import counting_frequency


def shift_symbol(symbol, shift):
    if symbol not in SYMBOLS_TO_POSITIONS:
        return symbol
    pos = SYMBOLS_TO_POSITIONS[symbol]
    assert isinstance(pos, int), pos
    pos = (pos + shift) % len(ALPHABET)
    return ALPHABET[pos]


def shift_text(text, shift):
    return "".join(shift_symbol(symbol, shift) for symbol in text)


def encode(input_text, key):
    return shift_text(input_text, key)


def decode(input_text, key):
    return shift_text(input_text, -key)


def hack(input_text, symbols_frequency):
    frequency_dict = counting_frequency.load_frequency(symbols_frequency)
    best_shift = 0
    best_dist = math.inf

    current_frequency_dict = counting_frequency.get_frequency_dict(input_text)

    for shift in range(len(ALPHABET)):
        current_dist = 0.0
        for i, symbol_in_this_text in enumerate(ALPHABET):
            symbol_in_shifted_text = ALPHABET[(i + shift) % len(ALPHABET)]
            diff = current_frequency_dict.get(symbol_in_this_text, 0) - frequency_dict.get(symbol_in_shifted_text, 0)
            current_dist += diff ** 2
        if current_dist < best_dist:
            best_dist = current_dist
            best_shift = shift

    return shift_text(input_text, best_shift)
