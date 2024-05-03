class LangueAnglaise:
    WELL_SAID = "Well said !"
    HELLO = "Hello"

    @classmethod
    def féliciter(cls):
        return cls.WELL_SAID

    @classmethod
    def saluer(cls):
        return cls.HELLO

    def __str__(self):
        return "Langue Anglaise"
