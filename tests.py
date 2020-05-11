import pytest
from encryptor import encrypt


def test_caesar_cipher():
    assert encrypt('caesar', 'encode', 'abb2', 2) == 'cdd2'
    assert encrypt('caesar', 'decode', 'cdd2', 2) == 'abb2'
    assert encrypt('caesar', 'hack', 'aaa') == '   '

def test_vigenere_cipher():
    assert encrypt('vigenere', 'encode', 'ATTACKATDAWN', 'LEMON') == '+[}./?$};-a;'
    assert encrypt('vigenere', 'decode', '+[}./?$};-a;', 'LEMON') == 'ATTACKATDAWN'

def test_with_empty_text():
    assert encrypt('caesar', 'encode', '', 123) == ''
    assert encrypt('caesar', 'decode', '', 123) == ''
    assert encrypt('caesar', 'hack', '') == ''
    assert encrypt('vigenere', 'encode', '', 'acfjwe') == ''
    assert encrypt('vigenere', 'decode', '', 'acfjwe') == ''
