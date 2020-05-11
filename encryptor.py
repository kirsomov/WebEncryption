import caesar_cipher
import vigenere_cipher


def encrypt(cipher, mode, input_text, key=None):
    if cipher == 'caesar':
        if mode == 'hack':
            return caesar_cipher.hack(input_text, "./symbols_frequency/symbols_frequency.pickle")
        key = int(key)
        if mode == 'encode':
            return caesar_cipher.encode(input_text, key)
        elif mode == 'decode':
            return caesar_cipher.decode(input_text, key)
    else:
        if mode == 'encode':
            return vigenere_cipher.encode(input_text, key)
        elif mode == 'decode':
            return vigenere_cipher.decode(input_text, key)
        elif mode == 'hack':
            return "Sorry, this function is not implemented"
