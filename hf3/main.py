print("Adja meg a háromszög három oldalát cm-ben:")
a = input("a oldal (cm):")
a = int(a)
b = input("b oldal (cm):")
b = int(b)
c = input("c oldal (cm):")
c = int(c)

if (a + b) > c and (b + c) > a and (c + a) > a:
    print("A háramszög szerkezthető!")
else:
    print("Nem szerkezthető!")
