from irasas import Irasas


class IslaiduIrasas(Irasas):
    """Sukuriame IslaiduIraso klase su savybemis"""

    def __init__(self, tipas, suma, atsiskaitymo_budas=None, isigyta_preke_paslauga=None):
        super().__init__(tipas, suma)
        self.atsiskaitymo_budas = atsiskaitymo_budas
        self.isigyta_preke_paslauga = isigyta_preke_paslauga
