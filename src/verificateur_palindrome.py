import os


class VérificateurPalindrome:
    BIEN_DIT = "Bien dit !"

    @classmethod
    def vérifier(cls, chaîne):
        miroir = chaîne[::-1]
        est_palindrome = miroir == chaîne

        return chaîne + os.linesep + cls.BIEN_DIT if est_palindrome else miroir
