def szekinit(szin: str, labszam: int):
    print(f"szin: {szin}, lábszám: {labszam}")

szekinit("kék", 3)
szekinit("prios", 4)
szekinit("zöld", 5)

def szekstr(szin: str, labszam: int):
    return (f"szin: {szin}, lábszám: {labszam}")

print(szekstr("kék", 3))
print(szekstr("piros", 4))
print(szekstr("zöld", 5))