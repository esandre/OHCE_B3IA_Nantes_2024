import os


class VérificateurPalindrome:
    BIEN_DIT = "Bien dit !"
    BONJOUR = "Bonjour"

    @classmethod
    def vérifier(cls, chaîne):
        miroir = chaîne[::-1]
        est_palindrome = miroir == chaîne

        retour = chaîne + os.linesep + cls.BIEN_DIT \
            if est_palindrome \
            else miroir

        return cls.BONJOUR + os.linesep + retour
