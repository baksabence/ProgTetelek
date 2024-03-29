from Szek import Szek

peldany = Szek("kék", 3)
peldanyketto = Szek("piros", 4)
peldanyharom = Szek("zöld", 5)
print(peldany.__str__())
print(peldanyketto)
print(peldanyharom)

szekek = [peldany, peldanyketto, peldanyharom]



def labakSzama():
    print("\nÖsszesen hány db láb van a teremben?", end="")
    ossz = 0
    for index in range(0, len(szekek), 1):
        ossz += szekek[index].labszam

    print(f"\n\tÖsszesen {ossz} láb van a teremben")

labakSzama()

# összegzés tétele
def maxLabSzin():
    maxIndex = 0
    print("\nMelyik színű széknek van a legtöbb lába?")
    for index in range(0, len(szekek), 1):
        if szekek[index].labszam > szekek[maxIndex].labszam:
            maxIndex = index

    print(f"\tA legtöbb lábbal rendelkező szék színe: {szekek[maxIndex].szin}")
maxLabSzin()

# maximum kiválasztás tétel

def negynelNagyobb():
    print("\nHány négynél több lábú szék van: ")
    db = 0
    for index in range(0, len(szekek), 1):
        if szekek[index].labszam > 4:
            db += 1
    print(f"\tA négynél több lábú székek száma : {db}")


negynelNagyobb()


# megszámlálás tétele



def pirosNegylabu():
    print("\n Van-e piros négy lábú szék: ")
    van = False
    for index in range(0, len(szekek), 1):
        if szekek[index].szin == "piros" and szekek[index].labszam == 4:
            van = True
    if van:
        print("\tvan")
    else:
        print("nincs")


pirosNegylabu()