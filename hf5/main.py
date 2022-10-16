class Developer:
        def __init__(self, Nev, Projekt, Szerepkor):
            self._Nev = Nev
            self._Projekt = Projekt
            self._Szerepkor = Szerepkor
            print(self.__str__())


        def get_Nev(self):
            return self._Nev

        def set_Nev(self, x):
            self._Nev = x

        def get_Projekt(self):
            return self._Projekt

        def set_Projekt(self, x):
            self._Projekt = x

        def get_Szerepkor(self):
            return self._Szerepkor

        def set_Szerepkor(self, x):
            self._Szerepkor = x


        def __str__(self):
            return self._Nev + " a " + self._Projekt + "-en dolgozik, a " + self._Szerepkor + " szrepkörbén."


        def __eq__(self, uj):
            return self._Projekt == uj._Projekt


        def egyProjekt(self, uj):

            if self.__eq__(uj):
                if(self._Nev != uj._Nev):
                 print(self._Nev + " és " + uj._Nev + " Egy projekten dolgoznak!")



dev = []
egyprojekt = Developer[]
dev1 = Developer("Ricsi", "Solarch", "Frontend")
dev2 = Developer("Anna", "Solarch", "Frontend")
dev3 = Developer("Anna", "Solarch", "Frontend")
Developer.egyProjekt(dev1, dev2)





