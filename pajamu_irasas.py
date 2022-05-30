from irasas import Irasas


class PajamuIrasas(Irasas):
    """Sukuriame PajamuIraso klase, su savybemis"""

    def __init__(self, tipas, suma, siuntejas=None, papildoma_informacija=None):
        super().__init__(tipas, suma)
        self.siuntejas = siuntejas
        self.papildoma_informacija = papildoma_informacija
