# test_vigenere_cipher.py
import unittest
from vigenere_cipher import encrypt_vigenere, decrypt_vigenere

class TestVigenereCipher(unittest.TestCase):
    
    def test_basic_encryption(self):
        self.assertEqual(encrypt_vigenere("HELLO", "KEY"), "RIJVS")
    
    def test_basic_decryption(self):
        self.assertEqual(decrypt_vigenere("RIJVS", "KEY"), "HELLO")
    
    def test_case_1(self):
        self.assertEqual(encrypt_vigenere("ATTACKATDAWN", "LEMON"), "LXFOPVEFRNHR")
        self.assertEqual(decrypt_vigenere("LXFOPVEFRNHR", "LEMON"), "ATTACKATDAWN")

    def test_case_2(self):
        self.assertEqual(encrypt_vigenere("VIGENERECIPHER", "KEY"), "FMEORCBIASTFOV")
        self.assertEqual(decrypt_vigenere("FMEORCBIASTFOV", "KEY"), "VIGENERECIPHER")
    
    def test_case_3(self):
        self.assertEqual(encrypt_vigenere("CRYPTOGRAPHY", "ABC"), "CSAPUQGSCPIA")
        self.assertEqual(decrypt_vigenere("CSAPUQGSCPIA", "ABC"), "CRYPTOGRAPHY")

    def test_case_with_spaces(self):
        self.assertEqual(encrypt_vigenere("ENCRYPT THIS MESSAGE", "KEY"), "ORABCNDXFSWKOWQKKC")
        self.assertEqual(decrypt_vigenere("ORABCNDXFSWKOWQKKC", "KEY"), "ENCRYPTTHISMESSAGE")
    
    def test_case_empty(self):
        self.assertEqual(encrypt_vigenere("", "KEY"), "")
        self.assertEqual(decrypt_vigenere("", "KEY"), "")

    def test_case_key_longer_than_text(self):
        self.assertEqual(encrypt_vigenere("HELLO", "LONGKEY"), "SSYRY")
        self.assertEqual(decrypt_vigenere("SSYRY", "LONGKEY"), "HELLO")

    def test_different_keys(self):
        # Пытаемся зашифровать один и тот же текст разными ключами, результат должен быть разным
        text = "HELLO"
        key1 = "KEY"
        key2 = "SECRET"
        
        encrypted_text1 = encrypt_vigenere(text, key1)
        encrypted_text2 = encrypt_vigenere(text, key2)
        
        self.assertNotEqual(encrypted_text1, encrypted_text2)

    def test_random_data(self):
        # Проверка на случайных данных
        import random
        import string
        
        random_text = ''.join(random.choices(string.ascii_uppercase, k=100))
        key = "RANDOMKEY"
        
        encrypted_text = encrypt_vigenere(random_text, key)
        decrypted_text = decrypt_vigenere(encrypted_text, key)
        
        self.assertEqual(decrypted_text, random_text)  # Шифрованный текст должен вернуться к исходному


if __name__ == '__main__':
    unittest.main()
