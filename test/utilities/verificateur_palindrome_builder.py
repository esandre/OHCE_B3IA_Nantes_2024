from utilities.une_langue_dont_on_se_fiche import UneLangueDontOnSeFiche
from verificateur_palindrome import VérificateurPalindrome


class VérificateurPalindromeBuilder:
    def build(self) -> VérificateurPalindrome:
        return VérificateurPalindrome(UneLangueDontOnSeFiche())

    @classmethod
    def par_defaut(cls):
        return VérificateurPalindromeBuilder().build()
