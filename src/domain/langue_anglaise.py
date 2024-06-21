from domain.moment_de_la_journee import MomentDeLaJournée


class LangueAnglaise:
    GOOD_EVENING = "Good evening"
    GOOD_NIGHT = "Good night"
    GOODBYE = "Goodbye"
    WELL_SAID = "Well said !"
    HELLO = "Hello"

    @classmethod
    def féliciter(cls):
        return cls.WELL_SAID

    @classmethod
    def saluer(cls, moment_de_la_journée):
        return cls.GOOD_NIGHT if moment_de_la_journée == MomentDeLaJournée.Nuit else cls.HELLO

    @classmethod
    def acquitter(cls):
        return cls.GOODBYE

    def __str__(self):
        return "Langue Anglaise"
