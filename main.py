import ertekek
import sorozat
import hatoslotto

#ertekek.elso_feldat1()

print("II/A,B,C")
listam=sorozat.veletlenABC() #az veletlenABC defben létrehozott listát hicom meg a main-be
print(f"\t", end="") #beljebb kezdeni a sorozatott
sorozat.kiir(listam)

print("II/D,E")
tizzel_db=sorozat.tizzel_oszthato(listam)
sorozat.konzol_ir(tizzel_db)
sorozat.fajlba_ir(tizzel_db)

print("III/A, B")
huzas_lista=hatoslotto.fajlbeolvas()
print(f"\tA húzások száma: {len(huzas_lista)}")

print("III/C")
atlag=hatoslotto.fajlbeolvas(huzas_lista)
print(f"\tA 42.héten húzott számok átlaga: {atlag}")

print("III/D")
max=hatoslotto.legnagyobb_kihuzott_szam(huzas_lista)
print(f"\tAz első legnagyobb kihuzott szam értéke: {huzas_lista[max].hely}, {huzas_lista[max].het},-ben, a {huzas_lista[max].ev}-ben, a {huzas_lista[max].het}.héten ki ez volt a {huzas_lista[max].huzas_id}.húzás")









