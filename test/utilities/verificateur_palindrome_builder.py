from utilities.une_langue_dont_on_se_fiche import UneLangueDontOnSeFiche
from verificateur_palindrome import VérificateurPalindrome


class VérificateurPalindromeBuilder:
    __langue = UneLangueDontOnSeFiche()

    @classmethod
    def par_defaut(cls):
        return VérificateurPalindromeBuilder().build()

    def build(self) -> VérificateurPalindrome:
        return VérificateurPalindrome(self.__langue)

    def ayant_pour_langue(self, langue):
        self.__langue = langue
        return self
