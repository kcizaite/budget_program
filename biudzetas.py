from islaidu_irasas import IslaiduIrasas
from pajamu_irasas import PajamuIrasas


class Biudzetas:
    """Sukuriamas Biudzeto klase su savybemis"""

    def __init__(self):
        self.zurnalas = []

    def __str__(self):
        return str(self.zurnalas)

    def prideti_pajamu_irasa(self, suma: int, siuntejas=None, papildoma_informacija=None):
        """Sukuriamas pajamu objektas su suma ir pridedamas i zurnala"""
        pajamos = PajamuIrasas("pajamos", suma, siuntejas, papildoma_informacija)
        self.zurnalas.append(pajamos)

    def prideti_islaidu_irasa(self, suma: int, atsiskaitymo_budas=None, isigyta_preke_paslauga=None):
        """Sukuriamas islaidu objektas su suma ir pridedamas i zurnala"""
        islaidos = IslaiduIrasas("islaidos", suma, atsiskaitymo_budas, isigyta_preke_paslauga)
        self.zurnalas.append(islaidos)

    def balansas(self):
        """Zurnalo sarase atskiriamos islaidos ir pajamos, jos susumuojamos.
        Gaunamas balansas is pajamu ir islaidu, grazinamas galutinis rezultatas"""
        islaidos = 0
        pajamos = 0
        for kitas_irasas in self.zurnalas:
            if isinstance(kitas_irasas, IslaiduIrasas):
                islaidos += kitas_irasas.suma
            elif isinstance(kitas_irasas, PajamuIrasas):
                pajamos += kitas_irasas.suma
        balansas = pajamos - islaidos
        return f"********************************************* \n" \
               f"Jusu Balansas (pateikiama euro valiuta): {balansas} \nTurimos pajamos: {pajamos}\n" \
               f"Esancios islaidos: {islaidos}"

    def parodyti_ataskaita(self):
        """Atspausdinamas zurnalo sarasas"""
        for irasas in self.zurnalas:
            if isinstance(irasas, IslaiduIrasas):
                print(
                    f"********************************************* \n"
                    f"Isigyta preke ir/ar paslauga: {irasas.isigyta_preke_paslauga}, "
                    f"atsiskaitymo budas: {irasas.atsiskaitymo_budas},"
                    f" {irasas.tipas} suma {irasas.suma}")
            elif isinstance(irasas, PajamuIrasas):
                print(f"********************************************* \n"
                      f"Siuntejas: {irasas.siuntejas}, papildoma informacija: {irasas.papildoma_informacija},"
                      f" {irasas.tipas} suma {irasas.suma}")
