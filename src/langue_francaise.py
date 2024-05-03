class LangueFrançaise:
    BIEN_DIT = "Bien dit !"

    @classmethod
    def féliciter(cls):
        return cls.BIEN_DIT

    def __str__(self):
        return "Langue Française"