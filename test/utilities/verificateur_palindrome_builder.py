from utilities.langue_stub import LangueStub
from domain.verificateur_palindrome import VérificateurPalindrome


class VérificateurPalindromeBuilder:
    __langue = LangueStub()
    __moment = None

    @classmethod
    def par_defaut(cls):
        return VérificateurPalindromeBuilder().build()

    def build(self) -> VérificateurPalindrome:
        return VérificateurPalindrome(self.__langue, self.__moment)

    def ayant_pour_moment_de_la_journée(self, moment):
        self.__moment = moment
        return self

    def ayant_pour_langue(self, langue):
        self.__langue = langue
        return self
