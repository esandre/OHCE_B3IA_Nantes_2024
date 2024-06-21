from datetime import datetime

from domain.moment_de_la_journee import MomentDeLaJournée


class MomentActuel:
    @staticmethod
    def déterminer():
        heure = datetime.now().hour
        return MomentDeLaJournée.depuis_heure(heure)