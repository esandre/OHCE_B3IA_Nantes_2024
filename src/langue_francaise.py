class LangueFrançaise:
    BIEN_DIT = "Bien dit !"
    BONJOUR = "Bonjour"

    @classmethod
    def féliciter(cls):
        return cls.BIEN_DIT

    @classmethod
    def saluer(cls):
        return cls.BONJOUR

    def __str__(self):
        return "Langue Française"
