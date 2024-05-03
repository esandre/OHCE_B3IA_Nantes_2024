import os
import random
import string
import unittest

from verificateur_palindrome import VérificateurPalindrome


class PalindromeTest(unittest.TestCase):
    @classmethod
    def randomword(cls, length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

    def test_miroir(self):
        cas = ["epsi", "test", "substance", self.randomword(10), self.randomword(100)]

        # ETANT DONNE un non-palindrome
        for chaîne in cas:
            with self.subTest(chaîne):
                # QUAND on vérifie si c'est un palindrome
                résultat = VérificateurPalindrome.vérifier(chaîne)

                # ALORS la chaîne est renvoyée en miroir
                attendu = chaîne[::-1]
                self.assertEqual(attendu, résultat)

    def test_bien_dit(self):
        # ETANT DONNE un palindrome
        palindrome = "radar"

        # QUAND on vérifie si c'est un palindrome
        résultat = VérificateurPalindrome.vérifier(palindrome)

        # ALORS la chaîne est renvoyée suivie de "Bien dit !"
        attendu = palindrome + os.linesep + "Bien dit !"
        self.assertEqual(attendu, résultat)


if __name__ == '__main__':
    unittest.main()
