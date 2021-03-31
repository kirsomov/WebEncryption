import pytest
from encryptor import encrypt
from alphabet import ALPHABET


def test_caesar_cipher():
    assert encrypt('caesar', 'encode', 'abb2', 2) == 'cdd2'
    assert encrypt('caesar', 'decode', 'cdd2', 2) == 'abb2'

    assert encrypt('caesar', 'encode', 'defgEM', -2) == 'bcdeCK'
    assert encrypt('caesar', 'decode', 'cdeabA', -2) == 'efgcdC'

    with open('./tests/text.txt') as input_file:
        input_text = input_file.read()
    for i in range(0, 50, 2):
        encrypted_text = encrypt('caesar', 'encode', input_text, i)
        assert encrypted_text == encrypt('caesar', 'decode', input_text, -i)
        if i != 0:
            assert encrypted_text != input_text
        assert encrypt('caesar', 'decode', encrypted_text, i) == input_text
        assert encrypt('caesar', 'hack', encrypted_text) == input_text


def test_vigenere_cipher():
    assert encrypt('vigenere', 'encode', 'aabdBE', 'ab') == 'abbeBF'
    assert encrypt('vigenere', 'decode', 'abbeBF', 'ab') == 'aabdBE'

    with open('./tests/text.txt') as input_file:
        input_text = input_file.read()

    key = 'afB wi!WEdjc#'
    assert encrypt('vigenere', 'decode', encrypt('vigenere', 'encode', input_text, key), key) == input_text

    assert encrypt('vigenere', 'encode', input_text, 'a') == input_text
    assert encrypt('vigenere', 'decode', input_text, 'a') == input_text

    assert encrypt('vigenere', 'encode', input_text, 'Le#') == encrypt('vigenere', 'encode', input_text, 'Le#Le#')
    assert encrypt('vigenere', 'decode', input_text, 'Le#') == encrypt('vigenere', 'decode', input_text, 'Le#Le#')


def test_with_empty_text():
    assert encrypt('caesar', 'encode', '', 123) == ''
    assert encrypt('caesar', 'decode', '', 123) == ''
    assert encrypt('caesar', 'hack', '') == ''
    assert encrypt('vigenere', 'encode', '', 'acfjwe') == ''
    assert encrypt('vigenere', 'decode', '', 'acfjwe') == ''
