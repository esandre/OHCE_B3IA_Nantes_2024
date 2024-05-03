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

    PALINDROME_REPRESENTATIF = "radar"
    NON_PALINDROME_REPRESENTATIF = "epsi"

    def test_miroir(self):
        cas = [self.NON_PALINDROME_REPRESENTATIF, "test", "substance", self.randomword(10), self.randomword(100)]

        # ETANT DONNE un non-palindrome
        for chaîne in cas:
            with self.subTest(chaîne):
                # QUAND on vérifie si c'est un palindrome
                résultat = VérificateurPalindrome.vérifier(chaîne)

                # ALORS la chaîne est renvoyée en miroir
                attendu = chaîne[::-1]
                self.assertIn(attendu, résultat)

    def test_bien_dit(self):
        # ETANT DONNE un palindrome
        palindrome = self.PALINDROME_REPRESENTATIF

        # QUAND on vérifie si c'est un palindrome
        résultat = VérificateurPalindrome.vérifier(palindrome)

        # ALORS la chaîne est renvoyée suivie de "Bien dit !"
        attendu = palindrome + os.linesep + VérificateurPalindrome.BIEN_DIT
        self.assertIn(attendu, résultat)

    def test_au_revoir(self):
        # ETANT DONNE une chaîne
        cas = [self.PALINDROME_REPRESENTATIF, self.NON_PALINDROME_REPRESENTATIF]

        for chaîne in cas:
            with self.subTest(chaîne):
                # QUAND on vérifie si c'est un palindrome
                résultat = VérificateurPalindrome.vérifier(chaîne)

                # ALORS la chaîne contient "Au revoir" sur la dernière ligne
                lignes = résultat.split(os.linesep)
                attendu = VérificateurPalindrome.AU_REVOIR
                self.assertEqual(attendu, lignes[-1])

    def test_bonjour(self):
        # ETANT DONNE une chaîne
        cas = [self.PALINDROME_REPRESENTATIF, self.NON_PALINDROME_REPRESENTATIF]

        for chaîne in cas:
            with self.subTest(chaîne):
                # QUAND on vérifie si c'est un palindrome
                résultat = VérificateurPalindrome.vérifier(chaîne)

                # ALORS la chaîne renvoyée est précédée de "Bonjour"
                lignes = résultat.split(os.linesep)
                attendu = VérificateurPalindrome.BONJOUR
                self.assertEqual(attendu, lignes[0])


if __name__ == '__main__':
    unittest.main()
