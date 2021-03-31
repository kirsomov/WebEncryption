from flask import Flask, flash, redirect, render_template, request, url_for
from encryptor import encrypt


class View:
    _TEMPLATE_PATH = "encryption.html"
    _MODES = ['hack', 'encode', 'decode']
    _CIPHERS = ['caesar', 'vigenere']
    _FORMATS = ['file', 'text']

    def __init__(self, input_format=None, output_format=None, cipher='caesar', mode='encode', input_text='', key='0'):
        self._input_format = input_format
        self._output_format = output_format
        self._cipher = cipher
        self._mode = mode
        self._input_text = input_text
        self._key = key
        self._output_text = ''

    def set_formats(self, input_format, output_format):
        self._input_format = input_format
        self._output_format = output_format

    def set_input_text(self, input_text):
        self._input_text = input_text

    def set_fields(self, cipher='caesar', mode='encode', input_text='', key=0):
        self._cipher = cipher
        self._mode = mode
        self._input_text = input_text
        if key:
            self._key = key
        elif cipher == 'caesar':
            self._key = '0'
        else:
            self._key = 'a'

    def get_input_format(self):
        return self._input_formaat

    def get_output_format(self):
        return self._output_format

    def get_input_text(self):
        return self._input_text

    def get_output_text(self):
        """Вычисляет выходной текст, если вернулся None, делает текст пустым"""
        self._output_text = encrypt(self._cipher, self._mode, self._input_text, self._key)
        return self._output_text

    def render_view(self):
        self.get_output_text()
        return render_template(
            self._TEMPLATE_PATH,
            input_formats=self._FORMATS,
            output_formats=self._FORMATS,
            modes=self._MODES,
            ciphers=self._CIPHERS,
            _input_format=self._input_format,
            _output_format=self._output_format,
            _cipher=self._cipher,
            _mode=self._mode,
            _key=self._key,
            input_text=self._input_text,
            output_text=self._output_text)
