import random
def veletlenABC():
    lista=[]
    for i in range  (0,8,1):
        vel=int(random.random()*959)-100
        lista.append(vel)
    return lista

def kiir(lista):
    for i in range(0,len(lista),1):
        if i == len(lista)-1: #utolsó elemnél nem lesz ; vessző
            print(lista[i])
        else:
            print(lista[i], end=";")

def tizzel_oszthato(lista):
    #megszamolas
    db:int=0
    i:int=0
    while i< len(lista):
        if lista[i] %10==0:
            db+=1
        i +=1
    return db

def konzol_ir(db):
    print(f"\t Tizzel oszthatok száma: {db}.")


def fajlba_ir(db):
    fajlnev:str="vegeredmeny.txt"
    print(f"\t Tizzel oszthatok száma: {db}")
    f = open(fajlnev, "w", encoding="utf-8")
    f.write(f"\t Tizzel oszthatok száma: {db}")
    f.close()
