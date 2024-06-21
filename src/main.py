from domain.verificateur_palindrome import VérificateurPalindrome
from langue_systeme import LangueSystème
from moment_actuel import MomentActuel

if __name__ == '__main__':
    langue = LangueSystème()
    moment = MomentActuel.déterminer()

    verificateur = VérificateurPalindrome(langue, moment)

    resultat = verificateur.vérifier("test")

    print(resultat)