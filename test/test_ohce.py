import os
import random
import string
import unittest

from domain.langue_anglaise import LangueAnglaise
from domain.langue_francaise import LangueFrançaise
from domain.moment_de_la_journee import MomentDeLaJournée
from utilities.langue_fake import LangueFake
from utilities.langue_stub import LangueStub
from utilities.verificateur_palindrome_builder import VérificateurPalindromeBuilder


class PalindromeTest(unittest.TestCase):
    @classmethod
    def randomword(cls, length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

    PALINDROME_REPRESENTATIF = "radar"
    NON_PALINDROME_REPRESENTATIF = "epsi"

    def test_miroir(self):
        cas = [self.NON_PALINDROME_REPRESENTATIF, "test", "substance", self.randomword(10), self.randomword(100)]

        # ETANT DONNE un non-palindrome
        for chaîne in cas:
            with self.subTest(chaîne):
                vérificateur = VérificateurPalindromeBuilder.par_defaut()

                # QUAND on vérifie si c'est un palindrome
                résultat = vérificateur.vérifier(chaîne)

                # ALORS la chaîne est renvoyée en miroir
                attendu = chaîne[::-1]
                self.assertIn(attendu, résultat)

    # Pas de Bien dit! quand pas de palindrome

    def test_féliciter(self):
        cas = [
            [LangueAnglaise(), LangueAnglaise.WELL_SAID],
            [LangueFrançaise(), LangueFrançaise.BIEN_DIT],
        ]

        for test in cas:
            langue = test[0]
            félicitations = test[1]

            with self.subTest(langue):
                # ETANT DONNE un palindrome
                palindrome = self.PALINDROME_REPRESENTATIF

                # ET que l'utilisateur parle un langue
                vérificateur = VérificateurPalindromeBuilder().ayant_pour_langue(langue).build()

                # QUAND on vérifie si c'est un palindrome
                résultat = vérificateur.vérifier(palindrome)

                # ALORS la chaîne est renvoyée suivie de "Bien dit !"
                attendu = palindrome + os.linesep + félicitations
                self.assertIn(attendu, résultat)

    # TODO : Vérifier l'absence de félicitations pour les non-palindromes

    def test_acquittance(self):
        cas = [
            [self.PALINDROME_REPRESENTATIF, LangueAnglaise(), LangueAnglaise.GOODBYE],
            [self.NON_PALINDROME_REPRESENTATIF, LangueAnglaise(), LangueAnglaise.GOODBYE],
            [self.PALINDROME_REPRESENTATIF, LangueFrançaise(), LangueFrançaise.AU_REVOIR],
            [self.NON_PALINDROME_REPRESENTATIF, LangueFrançaise(), LangueFrançaise.AU_REVOIR],
        ]

        for test in cas:
            chaîne = test[0]
            langue = test[1]
            acquittance = test[2]

            with self.subTest(f"{chaîne} - {langue}"):
                # ETANT DONNE une <chaîne>
                # ET que l'utilisateur parle <langue>

                # QUAND on vérifie si c'est un palindrome
                vérificateur = VérificateurPalindromeBuilder().ayant_pour_langue(langue).build()
                résultat = vérificateur.vérifier(chaîne)

                # ALORS la chaîne contient les salutations de cette langue sur la dernière ligne
                self.vérifier_dernière_ligne_égale(acquittance, résultat)

    def cas_test_bonjour(self):
        moments = [
            [MomentDeLaJournée.Inconnu],
            [MomentDeLaJournée.Nuit],
            [MomentDeLaJournée.Soir],
            [MomentDeLaJournée.Matin],
            [MomentDeLaJournée.AprèsMidi],
        ]

        chaines_testées = [self.PALINDROME_REPRESENTATIF, self.NON_PALINDROME_REPRESENTATIF]

        for moment in moments:
            for chaîne in chaines_testées:
                yield [chaîne, moment]

    def test_bonjour(self):
        cas = self.cas_test_bonjour()

        for test in cas:
            chaîne = test[0]
            moment = test[1]

            with self.subTest(f"{chaîne} - {moment}"):
                # ETANT DONNE une <chaîne>
                langue = LangueFake()

                # QUAND on vérifie si c'est un palindrome
                vérificateur = VérificateurPalindromeBuilder()\
                    .ayant_pour_langue(langue)\
                    .ayant_pour_moment_de_la_journée(moment)\
                    .build()

                résultat = vérificateur.vérifier(chaîne)
                attendu = langue.saluer(moment)

                self.vérifier_première_ligne_égale(attendu, résultat)

    def test_fin_ligne(self):
        cas = [LangueAnglaise(), LangueFrançaise(), LangueStub()]

        for langue in cas:
            with self.subTest(langue):
                chaîne = "test"

                verificateur_palindrome = VérificateurPalindromeBuilder()\
                    .ayant_pour_langue(langue)\
                    .build()

                résultat = verificateur_palindrome.vérifier(chaîne)

                self.assertTrue(résultat.endswith(os.linesep))

    def vérifier_ligne_égale(self, expected, result, line):
        lines = result.split(os.linesep)
        self.assertEqual(expected, lines[line])

    def vérifier_première_ligne_égale(self, expected, result):
        self.vérifier_ligne_égale(expected, result, 0)

    def vérifier_dernière_ligne_égale(self, expected, result):
        self.vérifier_ligne_égale(expected, result, -1)


if __name__ == '__main__':
    unittest.main()
