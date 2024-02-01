def mitcsinal():
    vege = 0
    db = 0
    min = 214747474747474444
    szam = int(input("szam: "))

    while szam < vege:
        if szam < min:
            min = szam
            db += 1
    print(db, "A számból a legnagyobb : ", min)

kivalaszto()
