import re

def format_text(text):
    """Leave only uppercase letters A-Z"""
    return ''.join([c.upper() for c in text if c.isalpha()])

def shift_letter(letter, shift):
    """Shift letter by shift positions in the alphabet"""
    return chr((ord(letter) - ord('A') + shift) % 26 + ord('A'))

def unshift_letter(letter, shift):
    """Reverse shift letter by shift positions"""
    return chr((ord(letter) - ord('A') - shift) % 26 + ord('A'))

def generate_vigenere_table():
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    table = []
    for i in range(26):
        row = alphabet[i:] + alphabet[:i]  # сдвигаем алфавит
        table.append(row)
    return table

def encrypt_vigenere(plaintext, key):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key = key.upper().replace(" ", "")  # удаляем пробелы из ключа
    plaintext = plaintext.upper().replace(" ", "")  # удаляем пробелы из текста
    key_repeated = (key * (len(plaintext) // len(key))) + key[:len(plaintext) % len(key)]
    table = generate_vigenere_table()
    
    ciphertext = []
    for p, k in zip(plaintext, key_repeated):
        row = alphabet.index(k)
        col = alphabet.index(p)
        ciphertext.append(table[row][col])
    
    return ''.join(ciphertext)

def decrypt_vigenere(ciphertext, key):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key = key.upper().replace(" ", "")  # удаляем пробелы из ключа
    ciphertext = ciphertext.upper().replace(" ", "")  # удаляем пробелы из шифртекста
    key_repeated = (key * (len(ciphertext) // len(key))) + key[:len(ciphertext) % len(key)]
    table = generate_vigenere_table()
    
    plaintext = []
    for c, k in zip(ciphertext, key_repeated):
        row = alphabet.index(k)
        col = table[row].index(c)
        plaintext.append(alphabet[col])
    
    return ''.join(plaintext)