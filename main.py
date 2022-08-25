from pojistenec import Pojistenec

pojistenci = []

pokracovat = "ano"

while pokracovat == "ano":
    try:
        moznost = int(
            input("\n---------------------------- \n     Evidence pojištěných    \n---------------------------- \n "
                  "Vyberte si akci: \n"
                  "1. Přidat nového pojištěného\n"
                  "2. Vypsat všechny pojištěné\n"
                  "3. Vyhledat pojištěnce\n"
                  "4. Ukončit aplikaci\n"
                  "Zadejte možnost:"))

        if moznost == 1:
            jmeno = input("Zadejte křestní jméno pojištěnce:")
            prijmeni = input("Zadejte přijmení pojištěnce:")
            tel_cislo = input("Zadejte telefonní číslo pojištěnce: ")

            novy_pojistenec = Pojistenec(jmeno, prijmeni, tel_cislo)
            print(novy_pojistenec)
            print("Pojištěnec byl nahrán.")
            pojistenci.append(novy_pojistenec)
            pokracovat = input("Přejete si pokračovat? ano/ne")

        elif moznost == 2:
            for pojistenec in pojistenci:
                print(pojistenec)
            pokracovat = input("Přejete si pokračovat? ano/ne")

        elif moznost == 3:
            zadane_jmeno = input("Zadejte jméno:")
            zadane_prijmeni = input('Zadejte přijmení:')
            for pojistenec in pojistenci:
                if pojistenec.jmeno == zadane_jmeno and pojistenec.prijmeni == zadane_prijmeni:
                    print(pojistenec)
                    print("Pojištěnec existuje")
                else:
                    print("Pojištěnec nebyl nalezen")
            pokracovat = input("Přejete si pokračovat? ano/ne")

        elif moznost == 4:
            pokracovat = "Ne"

        else:
            print("Zadali jste nesprávnou možnost.")
            pokracovat = input("Přejete si pokračovat? ano/ne")

    except ValueError as v:  # Pro případ kdyby se zadal string místo integeru do inputu
        print("Zadali jste nesprávnou možnost.")
        pokracovat = input("Přejete si pokračovat? ano/ne")

konec = input("Aplikace se uzavře stiskem libovolné klávesy")
