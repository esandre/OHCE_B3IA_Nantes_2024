from domain.moment_de_la_journee import MomentDeLaJournée
from domain.verificateur_palindrome import VérificateurPalindrome
from langue_systeme import LangueSystème

if __name__ == '__main__':
    langue = LangueSystème()
    moment = MomentDeLaJournée.Nuit

    verificateur = VérificateurPalindrome(langue, moment)

    resultat = verificateur.vérifier("test")

    print(resultat)