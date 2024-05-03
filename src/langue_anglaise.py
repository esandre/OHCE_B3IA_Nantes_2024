class LangueAnglaise:
    GOODBYE = "Goodbye"
    WELL_SAID = "Well said !"
    HELLO = "Hello"

    @classmethod
    def féliciter(cls):
        return cls.WELL_SAID

    @classmethod
    def saluer(cls):
        return cls.HELLO

    @classmethod
    def acquitter(cls):
        return cls.GOODBYE

    def __str__(self):
        return "Langue Anglaise"
