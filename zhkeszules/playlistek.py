def beolvas():
    zenek = []

    with open("playlist.csv", "r") as f:
        sorok = f.readlines()

        for sor in sorok:
            sor = sor.strip()
            darabok = sor.split(";")
            zene = {"eloado": darabok[0], "cim": darabok[1], "mufaj": darabok[2], "hossz": int(darabok[3])}
            zenek.append(zene)

    return zenek


# masodik feladat
def hosszosszeg(zenek):
    hossz = 0

    for zene in zenek:
        hossz += zene["hossz"]

    hossz_percben = hossz // 60
    hossz_masodpercben = hossz % 60

    with open("osszhossz.txt", "w") as f:
        f.write(f"A lejatszasi lista hossza: {hossz_percben} perc, {hossz_masodpercben} masodperc\n")


# harmadik feladat
def leghosszabb_rockzene(zenek):
    max_hossz = 0
    leghosszabb_rock_cime = ""

    for zene in zenek:
        if zene["mufaj"] == "rock" and zene["hossz"] > max_hossz:
            max_hossz = zene["hossz"]
            leghosszabb_rock_cime = zene["cim"]

    with open("leghosszabbrock.txt", "w") as f:
        f.write(f"{leghosszabb_rock_cime}\n")


# negyedik feladat
def leggyakoribb_mufaj(zenek):
    mufajszamolas = {}

    for zene in zenek:
        mufaj = zene["mufaj"].upper()

        if mufaj not in mufajszamolas:
            mufajszamolas[mufaj] = 1
        else:
            mufajszamolas[mufaj] += 1

    max = 0
    leggyakoribb = ""

    for mufaj, elofordulas in mufajszamolas.items():
        if elofordulas > max:
            max = elofordulas
            leggyakoribb = mufaj

    with open("leggyakoribbmufaj.txt", "w") as f:
        f.write(f"{leggyakoribb}\n")

# otodik feladat

def zenecsoportositas(zenek):
    zeneeloadokent = {}

    for zene in zenek:
        eloado = zene["eloado"]
        hossz = zene["hossz"]

        if eloado not in zeneeloadokent:
            zeneeloadokent[eloado] = hossz
        else:
            zeneeloadokent[eloado] += hossz

    with open("zenehosszak.txt", "w") as f:
        for eloado, hossz in sorted(zeneeloadokent.items()):
            f.write(f"{eloado} - eloadonak osszesen {hossz} masodpercnyi zene van a listaban\n")


# hatodik feladat

def zene_listazas(zenek, eloado):
    fajlnev = eloado.lower().replace(" ", "_") + "_zene.txt"
    eloadozenek = []

    for zene in zenek:
        if zene["eloado"].lower() == eloado.lower():
            eloadozenek.append(zene)

    with open(fajlnev, "w") as f:
        if len(eloadozenek) == 0:
                f.write(f"Nincs ilyen eloado a lejatszasi listaban!\n")
        else:
            for zene in eloadozenek:
                f.write(f"{zene['cim']};{zene['mufaj']};{zene['hossz']}\n")


# hetedik feladat

def zenetorles(zenek, eloadok):
    with open("toroltzene.txt", "w") as f:
        for zene in zenek:
            if zene["eloado"] not in eloadok:
                f.write(f"{zene['eloado']};{zene['cim']};{zene['mufaj']};{zene['hossz']}\n")


if __name__ == '__main__':

    #1 feladat lehivasa
    lejatszasi_lista = beolvas()
    #2ik feladat lehivasa
    hosszosszeg(lejatszasi_lista)
    #3ik feladat lehivasa
    leghosszabb_rockzene(lejatszasi_lista)
    #4ik feladat lehivasa
    leggyakoribb_mufaj(lejatszasi_lista)
    #5ik feladat lehivasa
    zenecsoportositas(lejatszasi_lista)
    #6ik feladat lehivasa
    zene_listazas(lejatszasi_lista, 'Rick Astley')
    #7ik feladat lehivasa
    zenetorles(lejatszasi_lista, "Dschinghis Khan")