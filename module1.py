import os
from gtts import gTTS
def failist_lugemine(f:str,l:list):
    """Info failist f listisse l
    """
    fail=open(f,"r",encoding="utf-8-sig") #,encoding="utf-8-sig"
    for rida in fail:
        l.append(rida.trip())#"\n"
    fail.close()
    return l
def failisse_salvestamine(f:str,l:list):
    """Loetelu salvestame failisse
    """
    fail=open(f,"w")
    for el in l:
        fail.write(el+"\n")
    fail.close()
def rida_salvestamine(f:str,rida:str):
    """Üks sõna või lause(rida) salvestame failisse
    :param str f:fail kuku salvestame
    :param str rida: sõna, mis vaja salvestada failisse
    """
    fail=open(f,"a")
    fail.write(rida+"\n")
    fail.close()
def uus_sona(f:str,rida:str)->list:
    """Lisame uus sõna failisse ja listisse
    :param str file: Faili nimetus
    :param str x: lisatav sõna
    """

    l=[]
    with open(f,"a",encoding="utf-8-sig") as fail:
        fail.write(rida+"\n")
        l=failist_lugemine(f)
        return l
def tolkimine(l1:list,l2:list):
    sona=input("Mida tõlkida?")
    if sona in l1:
        tolk=l2[l1.index(sona)]
        print(sona+"-"+tolk)
    elif sona in l2:
        tolk=l2[l1.index(sona)]
        print(sona+"-"+tolk)
    else:
        print("Sõna puudub sõnastikus!")
def viga(l1:list,l2:list):
    sona=input("Sõna veaga?")
    if sona not in l1 and soan not in l2:
        print("Sõna puudub")
    else:
        if sona in l1:
            tolk=l2[l1.index(sona)]
            l1.remove(sona)
            l2.remove(tolk)
        elif sona in l2:
            tolk=l1[l2.index(sona)]
            l1.remove(sona)
            l2.remove(tolk)
        l1.append(input("Введи новое слово: "))
        l2.append(input("Введи новое слово: "))
        failisse_salvestamine(f1,l1)
        failisse_salvestamine(f2,l2)

def heli(text:str,keel:str):
    obj=gTTS(text=text,lang)

