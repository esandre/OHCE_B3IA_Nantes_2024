import os


class VérificateurPalindrome:
    AU_REVOIR = "Au revoir"

    def __init__(self, langue):
        self.__langue = langue
        pass

    def vérifier(self, chaîne):
        miroir = chaîne[::-1]
        est_palindrome = miroir == chaîne

        félicitations = self.__langue.féliciter()
        salutations = self.__langue.saluer()

        retour = chaîne \
            if est_palindrome \
            else miroir

        return salutations + os.linesep + retour + os.linesep + félicitations + os.linesep + self.AU_REVOIR
