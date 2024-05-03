import os


class VérificateurPalindrome:
    def __init__(self, langue):
        self.__langue = langue
        pass

    def vérifier(self, chaîne):
        miroir = chaîne[::-1]
        est_palindrome = miroir == chaîne

        félicitations = self.__langue.féliciter()
        salutations = self.__langue.saluer()
        acquittance = self.__langue.acquitter()

        retour = chaîne \
            if est_palindrome \
            else miroir

        return (salutations + os.linesep
                + retour + os.linesep
                + félicitations + os.linesep
                + acquittance)
