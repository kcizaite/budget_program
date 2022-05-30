class Irasas():
    """Sukuriama Iraso klase su savybemis"""
    def __init__(self, tipas, suma):
        self.tipas = tipas
        self.suma = suma

    def __str__(self):
        return f"tipas: {self.tipas}, suma: {self.suma}"