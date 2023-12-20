from Lottoszam import Lottoszam
def fajlbeolvas():
    huzas_lista=[] #itt leszenk a huzott számok osztálya
    f=open("huzasok.txt", "r",encoding="UTF-8")
    f.readline()
    szoveg_lista=f.readlines()
    for i in range (0,len(szoveg_lista),1):
       #szoveg listának az [i] eleme =
        sor_lista=szoveg_lista[i].strip().split("@")
        #példányositom az osztályomat
        lottoszam=Lottoszam(int(sor_lista[0]), int (sor_lista[1]),int(sor_lista[2]), int(sor_lista[3]))
        huzas_lista.append(lottoszam)

    return huzas_lista

def huzottszamok_atlaga_43(lista):
    #megszamlas és összegzes tetele
    db:int=0
    osszeg:int=0
    for i in range(0,len(lista),1):

        if lista[i].huzas_id==42:
            db+=1
            osszeg+=lista[i].szam

    atlag:float=osszeg/db
    return atlag


def legnagyobb_kihuzott_szam(lista):
    #maximum kivalasztas
    max: int = 0
    osszeg: int = 0
    for i in range(0, len(lista), 1):

        if lista[i].szam > lista[max].hely:
            #a maximum érték helyét keresük
            max=i

    return max
