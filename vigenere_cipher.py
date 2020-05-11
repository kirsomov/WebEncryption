import string
import pickle
from alphabet import ALPHABET
from alphabet import SYMBOLS_TO_POSITIONS


def get_encrypted_symbol_pos(symbol_pos, key_symbol_pos):
    return (symbol_pos + key_symbol_pos) % len(ALPHABET)


def get_decrypted_symbol_pos(symbol_pos, key_symbol_pos):
    alphabet_length = len(ALPHABET)
    return (symbol_pos - key_symbol_pos + alphabet_length) % alphabet_length


# в зависимости от переданной функции возвращает зашифрованный или дешифрованный символ
# передаваемая функция должна принимать два аргумента symbol и key_symbol
# в данной программе используется (и должно использоваться только)
# только функции get_decrypted_symbol_pos and get_encrypted_symbol_pos
def get_symbol_by_function(symbol, key_symbol, func):
    assert func == get_encrypted_symbol_pos or func == get_decrypted_symbol_pos, "incorrect index retrieval function"
    if symbol not in SYMBOLS_TO_POSITIONS:
        return symbol
    symbol_pos = SYMBOLS_TO_POSITIONS[symbol]
    key_symbol_pos = SYMBOLS_TO_POSITIONS[key_symbol]
    return ALPHABET[func(symbol_pos, key_symbol_pos)]


def get_encrypted_symbol(symbol, key_symbol):
    return get_symbol_by_function(symbol, key_symbol, get_encrypted_symbol_pos)


def get_decrypted_symbol(symbol, key_symbol):
    return get_symbol_by_function(symbol, key_symbol, get_decrypted_symbol_pos)


# аналогично get_symbol_by_function
# используется для get_encrypted_symbol, get_decrypted_symbol
def code(text, key, func):
    assert func == get_encrypted_symbol or func == get_decrypted_symbol, "incorrect index retrieval function"
    return "".join(func(text[i], key[i % len(key)]) for i in range(len(text)))


def encode(text, key):
    return code(text, key, get_encrypted_symbol)


def decode(text, key):
    return code(text, key, get_decrypted_symbol)
