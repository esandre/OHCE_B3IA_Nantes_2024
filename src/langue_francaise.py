class LangueFrançaise:
    BIEN_DIT = "Bien dit !"
    BONJOUR = "Bonjour"
    AU_REVOIR = "Au revoir"

    @classmethod
    def féliciter(cls):
        return cls.BIEN_DIT

    @classmethod
    def saluer(cls):
        return cls.BONJOUR

    @classmethod
    def acquitter(cls):
        return cls.AU_REVOIR

    def __str__(self):
        return "Langue Française"
