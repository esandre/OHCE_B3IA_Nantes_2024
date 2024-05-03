import os


class VérificateurPalindrome:
    BONJOUR = "Bonjour"
    AU_REVOIR = "Au revoir"

    def __init__(self, langue):
        self.__langue = langue
        pass

    def vérifier(self, chaîne):
        miroir = chaîne[::-1]
        est_palindrome = miroir == chaîne

        félicitations = self.__langue.féliciter()

        retour = chaîne + os.linesep + félicitations \
            if est_palindrome \
            else miroir

        return self.BONJOUR + os.linesep + retour + os.linesep + self.AU_REVOIR
