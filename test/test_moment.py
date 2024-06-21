import unittest

from domain.moment_de_la_journee import MomentDeLaJournée


class TestMoment(unittest.TestCase):
    def test_moment_selon_heure(self):
        cas = [
            [0, MomentDeLaJournée.Nuit],
            [7, MomentDeLaJournée.Nuit],
            [8, MomentDeLaJournée.Matin],
            [11, MomentDeLaJournée.Matin],
            [12, MomentDeLaJournée.AprèsMidi],
            [17, MomentDeLaJournée.AprèsMidi],
            [18, MomentDeLaJournée.Soir],
            [20, MomentDeLaJournée.Soir],
            [21, MomentDeLaJournée.Nuit],
            [23, MomentDeLaJournée.Nuit],
        ]

        for params in cas:
            heure = params[0]
            moment_attendu = params[1]
            with self.subTest(f"{heure} -> {moment_attendu}"):
                moment_obtenu = MomentDeLaJournée.depuis_heure(heure)
                self.assertEqual(moment_attendu, moment_obtenu)