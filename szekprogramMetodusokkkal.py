from Szek import Szek

peldany = Szek("kék", 3)
peldanyketto = Szek("piros", 4)
peldanyharom = Szek("zöld", 5)


szekek = [peldany, peldanyketto, peldanyharom]

def peldanyokListaban():
    peldany = Szek("kék", 3)
    peldanyketto = Szek("piros", 4)
    peldanyharom = Szek("zöld", 5)
    szekek = [peldany, peldanyketto, peldanyharom]
    return szekek



szekLista = peldanyokListaban()

def osszegzesTetele(szekek):
    print("\nÖsszesen hány db láb van a teremben?", end="")
    ossz = 0
    for index in range(0, len(szekek), 1):
        ossz += szekek[index].labszam

    print(f"\n\tÖsszesen {ossz} láb van a teremben")



def maxKivalasztasTetele(szekek):
    maxIndex = 0
    print("\nMelyik színű széknek van a legtöbb lába?")
    for index in range(0, len(szekek), 1):
        if szekek[index].labszam > szekek[maxIndex].labszam:
            maxIndex = index

    print(f"\tA legtöbb lábbal rendelkező szék színe: {szekek[maxIndex].szin}")



def megszamlalasTetele(szekek):
    print("\nHány négynél több lábú szék van: ")
    db = 0
    for index in range(0, len(szekek), 1):
        if szekek[index].labszam > 4:
            db += 1
    print(f"\tA négynél több lábú székek száma : {db}")





def eldontesTetele(szekek):
    print("\n Van-e piros négy lábú szék: ")
    van = False
    for index in range(0, len(szekek), 1):
        if szekek[index].szin == "piros" and szekek[index].labszam == 4:
            van = True
    if van:
        print("\tvan")
    else:
        print("nincs")







def listakiir(lista):
    for index in range(0, len(lista), 1):
        print(szekek[index])


# rovid verzio
listakiir(peldanyokListaban())


# hosszu verzio


osszegzesTetele(szekLista)
maxKivalasztasTetele(szekLista)
megszamlalasTetele(szekLista)
eldontesTetele(szekLista)


listakiir(szekLista)





