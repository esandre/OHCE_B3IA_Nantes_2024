import unittest

from verificateur_palindrome import VérificateurPalindrome


class PalindromeTest(unittest.TestCase):
    def test_miroir(self):
        # ETANT DONNE un non-palindrome
        chaîne = "epsi"

        # QUAND on vérifie si c'est un palindrome
        résultat = VérificateurPalindrome.vérifier(chaîne)

        # ALORS la chaîne est renvoyée en miroir
        self.assertEqual("ispe", résultat)


if __name__ == '__main__':
    unittest.main()
