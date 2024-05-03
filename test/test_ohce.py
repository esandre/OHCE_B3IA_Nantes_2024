import unittest

from verificateur_palindrome import VérificateurPalindrome


class PalindromeTest(unittest.TestCase):
    def test_miroir(self):
        cas = ["epsi", "test"]

        # ETANT DONNE un non-palindrome
        for chaîne in cas:
            with self.subTest(chaîne):
                # QUAND on vérifie si c'est un palindrome
                résultat = VérificateurPalindrome.vérifier(chaîne)

                # ALORS la chaîne est renvoyée en miroir
                attendu = chaîne[::-1]
                self.assertEqual(attendu, résultat)


if __name__ == '__main__':
    unittest.main()
