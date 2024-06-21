from domain.moment_de_la_journee import MomentDeLaJournée


class LangueFrançaise:
    BONSOIR = "Bonsoir"
    BIEN_DIT = "Bien dit !"
    BONJOUR = "Bonjour"
    AU_REVOIR = "Au revoir"

    @classmethod
    def féliciter(cls):
        return cls.BIEN_DIT

    @classmethod
    def saluer(cls, moment):
        return cls.BONSOIR if moment == MomentDeLaJournée.Nuit else cls.BONJOUR

    @classmethod
    def acquitter(cls):
        return cls.AU_REVOIR

    def __str__(self):
        return "Langue Française"
