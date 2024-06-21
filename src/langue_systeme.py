import locale

from domain.langue_anglaise import LangueAnglaise
from domain.langue_francaise import LangueFrançaise


class LangueSystème:
    def __init__(self):
        langue_système = locale.getlocale()[0]
        self.__langueUtilisateur = LangueAnglaise() if langue_système == "en_GB" else LangueFrançaise()

    def féliciter(self):
        return self.__langueUtilisateur.féliciter()

    def saluer(self, moment):
        return self.__langueUtilisateur.saluer(moment)

    def acquitter(self):
        return self.__langueUtilisateur.acquitter()