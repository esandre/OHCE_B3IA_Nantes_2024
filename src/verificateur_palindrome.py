import os


class VérificateurPalindrome:
    @classmethod
    def vérifier(cls, chaîne):
        miroir = chaîne[::-1]
        est_palindrome = miroir == chaîne

        return chaîne + os.linesep + "Bien dit !" if est_palindrome else miroir
