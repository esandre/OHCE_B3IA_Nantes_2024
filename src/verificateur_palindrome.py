import os


class VérificateurPalindrome:
    def __init__(self, langue, moment):
        self.__moment = moment
        self.__langue = langue

    def vérifier(self, chaîne):
        miroir = chaîne[::-1]
        est_palindrome = miroir == chaîne

        félicitations = self.__langue.féliciter()
        salutations = self.__langue.saluer(self.__moment)
        acquittance = self.__langue.acquitter()

        retour = chaîne \
            if est_palindrome \
            else miroir

        return (salutations + os.linesep
                + retour + os.linesep
                + félicitations + os.linesep
                + acquittance)
