from Szek import Szek

peldany = Szek("kék", 3)
peldanyketto = Szek("piros", 4)
peldanyharom = Szek("zöld", 5)
print(peldany.__str__())
print(peldanyketto)
print(peldanyharom)

szekek = [peldany, peldanyketto, peldanyharom]



def labakSzama():
    print("Összesen hány db láb van a teremben?", end="")
    ossz = 0
    for index in range(0, len(szekek), 1):
        ossz += szekek[index].labszam

    print(f"Összesen {ossz} láb van a teremben")

labakSzama()

def maxLabSzin():
    maxIndex = 0
    print("Melyik színű széknek van a legtöbb lába?")
    for index in range(0, len(szekek), 1):
        if szekek[index].labszam > szekek[maxIndex].labszam:
            maxIndex = index

    print(f"A legtöbb lábbal rendelkező szék színe: {szekek[maxIndex].szin}")
maxLabSzin()
