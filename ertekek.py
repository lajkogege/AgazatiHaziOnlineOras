def elso_feldat1():
    nap:str=input("Add meg a hét napját: ")
    ora_neve: str = input("Add meg az óra nevét: ")
    ertekeles: int = int(input("Add meg az értékelést: "))
    if (ertekeles<0):
        print(f"Az értékelés nem lehet negatív")
    elif(ertekeles > 5):
        print(f"Az értékelés nem elfogadható!")
    else:
        print(f"Köszönjük az értékelést!")

    print(f"I/A,B")
    print(f"\tHét napja: {nap}") #\t beljebb kezdes
    print(f"\tÓra neve: {ora_neve}")
    print(f"\tÉrtékelés (0-5): {ertekeles}")