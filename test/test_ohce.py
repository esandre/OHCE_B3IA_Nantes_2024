import os
import random
import string
import unittest

from langue_anglaise import LangueAnglaise
from langue_francaise import LangueFrançaise
from utilities.verificateur_palindrome_builder import VérificateurPalindromeBuilder
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
                vérificateur = VérificateurPalindromeBuilder.par_defaut()

                # QUAND on vérifie si c'est un palindrome
                résultat = vérificateur.vérifier(chaîne)

                # ALORS la chaîne est renvoyée en miroir
                attendu = chaîne[::-1]
                self.assertIn(attendu, résultat)

    def test_féliciter(self):
        cas = [
            [LangueAnglaise(), LangueAnglaise.WELL_SAID],
            [LangueFrançaise(), LangueFrançaise.BIEN_DIT]
        ]

        for test in cas:
            langue = test[0]
            félicitations = test[1]

            with self.subTest(langue):
                # ETANT DONNE un palindrome
                palindrome = self.PALINDROME_REPRESENTATIF

                # ET que l'utilisateur parle un langue
                vérificateur = VérificateurPalindromeBuilder().ayant_pour_langue(langue).build()

                # QUAND on vérifie si c'est un palindrome
                résultat = vérificateur.vérifier(palindrome)

                # ALORS la chaîne est renvoyée suivie de "Bien dit !"
                attendu = palindrome + os.linesep + félicitations
                self.assertIn(attendu, résultat)

    def test_au_revoir(self):
        # ETANT DONNE une chaîne
        cas = [self.PALINDROME_REPRESENTATIF, self.NON_PALINDROME_REPRESENTATIF]

        for chaîne in cas:
            with self.subTest(chaîne):
                # QUAND on vérifie si c'est un palindrome
                vérificateur = VérificateurPalindromeBuilder.par_defaut()
                résultat = vérificateur.vérifier(chaîne)

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
                vérificateur = VérificateurPalindromeBuilder.par_defaut()
                résultat = vérificateur.vérifier(chaîne)

                # ALORS la chaîne renvoyée est précédée de "Bonjour"
                lignes = résultat.split(os.linesep)
                attendu = VérificateurPalindrome.BONJOUR
                self.assertEqual(attendu, lignes[0])


if __name__ == '__main__':
    unittest.main()
