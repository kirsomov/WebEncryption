from alphabet import SYMBOLS_TO_POSITIONS
import caesar_cipher
import vigenere_cipher


def encrypt(cipher, mode, input_text, key=None):
    if cipher == 'caesar':
        if mode == 'hack':
            return caesar_cipher.hack(input_text, "./symbols_frequency/symbols_frequency.pickle")
        try:
            key = int(key)
        except Exception as e:
            return "For caesar's cipher, the key must be an integer"
        if mode == 'encode':
            return caesar_cipher.encode(input_text, key)
        elif mode == 'decode':
            return caesar_cipher.decode(input_text, key)
    else:
        for symbol in key:
            if symbol not in SYMBOLS_TO_POSITIONS:
                return "Symbol '" + symbol + "' not in alphabet"
        if mode == 'encode':
            return vigenere_cipher.encode(input_text, key)
        elif mode == 'decode':
            return vigenere_cipher.decode(input_text, key)
        elif mode == 'hack':
            return "Sorry, this function is not implemented"
