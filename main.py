from biudzetas import Biudzetas


def minibiudzeto_programa():
    """Vartotojo programa per console"""
    biudzetas = Biudzetas()
    print("____________MINI BIUDZETO PROGAMA____________\n")
    while True:
        pasirinkimas = input("*********************MENU******************** \n"
                             "Pasirinkite is zemiau pateiktu funkciju: \n"
                             "1: Prideti PAJAMAS arba ISLAIDAS su suma \n"
                             "2: Balansas \n"
                             "3: Ataskaita \n"
                             "4: Iseiti \n"
                             "Pasirinkimas: \n")
        if pasirinkimas == "4":
            print("********************************************* \n"
                  "Jusu darbas baigtas. Dekojame, kad naudojotes musu paslaugomis.")
            break
        if pasirinkimas == "1":
            tipas = input("********************************************* \n"
                          "Prasome nurodyti, ka norite prideti:\n1: Pajamas\n"
                          "2: Islaidas\nPasirinkimas ")

            if tipas == "1":
                siuntejas = input("Iveskite siunteja ")
                papildoma_informacija = input("Iveskite papildoma informacija ")
                suma = int(input("Iveskite suma \nPasirinkimas "))
                biudzetas.prideti_pajamu_irasa(suma, siuntejas, papildoma_informacija)
            if tipas == "2":
                atsiskaitymo_budas = input("Iveskite atsiskaitymo buda ")
                isigyta_preke_paslauga = input("Iveskite isigyta preke ir/ar paslauga ")
                suma = int(input("Iveskite suma \nPasirinkimas "))
                biudzetas.prideti_islaidu_irasa(suma, atsiskaitymo_budas, isigyta_preke_paslauga)

        if pasirinkimas == "2":
            print(biudzetas.balansas())
        if pasirinkimas == "3":
            biudzetas.parodyti_ataskaita()


if __name__ == '__main__':
    minibiudzeto_programa()
