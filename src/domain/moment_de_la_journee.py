import enum


class MomentDeLaJournée(enum.Enum):
    AprèsMidi = 4
    Matin = 3
    Soir = 2
    Nuit = 0
    Inconnu = 1

    @classmethod
    def depuis_heure(cls, heure):
        if heure < 8:
            return MomentDeLaJournée.Nuit
        if heure < 12:
            return MomentDeLaJournée.Matin
        if heure < 18:
            return MomentDeLaJournée.AprèsMidi
        if heure < 21:
            return MomentDeLaJournée.Soir

        return MomentDeLaJournée.Nuit
