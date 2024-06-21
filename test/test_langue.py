import unittest

from domain.langue_anglaise import LangueAnglaise
from domain.moment_de_la_journee import MomentDeLaJournée


class TestLangue(unittest.TestCase):
    def test_langue_anglaise_salutation(self):
        cas = [
            MomentDeLaJournée.Nuit, LangueAnglaise.GOOD_NIGHT,
            MomentDeLaJournée.Soir, LangueAnglaise.GOOD_EVENING,
            MomentDeLaJournée.AprèsMidi, LangueAnglaise.GOOD_AFTERNOON,
            MomentDeLaJournée.Matin, LangueAnglaise.GOOD_MORNING,
            MomentDeLaJournée.Inconnu, LangueAnglaise.HELLO,
        ]

        for params in cas:
            moment = params[0]
            saluations_attendues = params[1]

            with self.subTest(f"{moment} -> {saluations_attendues}"):
                self.assertEqual(LangueAnglaise.saluer(moment), saluations_attendues)