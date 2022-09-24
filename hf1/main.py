from collections import defaultdict

mondat = input ("Adjon meg egy mondatot!\n")

gyakorisag = defaultdict(int) # az ertekeket alapbol intekre fogja allitani

for i in mondat:
    gyakorisag[i] += 1


print(gyakorisag)