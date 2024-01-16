def elso():
    n = -1
    i = 0
    ossz = 0

    while n < 0:
        n = int(input(" N = "))

    for i in range(0, n+1, 1):

        ossz += 1
    print(f"Az első {n} db természetes szám összege: {ossz}")