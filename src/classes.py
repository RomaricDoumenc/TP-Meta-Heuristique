class Item:
    def __init__(self, weight, color, objId):
        self.weight = weight
        self.color = color
        self.id = objId

    def __str__(self):
        return "[Objet {} : Poids = {} , Couleur = {}]".format(self.id, self.weight, self.color)


class Box:
    def __init__(self, cap, idBox):
        self.listObj = []
        self.cap = int(cap)
        self.id = idBox

    def capResiduelle(self):
        """Capacité restante dans la boite."""
        capRes = int(self.cap)
        for item in self.listObj:
            capRes -= int(item.weight)
        return int(capRes)

    def addItem(self, item):
        """Ajoute un objet dans la boite s'il reste suffisamment de place et si 
        la contrainte de 2 couleurs maximum est respectée."""

        if self.capResiduelle() - int(item.weight) < 0:
            print("Impossible d'ajouter l'objet " + str(item) + " : pas assez de place dans la boite.")
            return False

        lcolors = self.listColors()

        if len(lcolors) >= 2:
            try:
                lcolors.index(item.color)
            except ValueError:
                print("Impossible d'ajouter l'objet " + str(item) + " : 2 couleurs maximum.")
                return False

        self.listObj.append(item)

        return True

    def dellItem(self, idObj):
        """Supprime un objet selon son id."""
        for item in self.listObj:
            if item.id == idObj:
                self.listObj.remove(item)
                return True
        return False

    def __str__(self):
        chaine = 'Boite {} '.format(self.id)
        for item in self.listObj:
            chaine += str(item) + " ; "
        chaine += "Capacité restante = " + str(self.capResiduelle())
        return chaine

    def listColors(self):
        """Retourne le nombre de couleurs différentes des objets de la boite."""
        listeCoul = []
        for item in self.listObj:
            try:
                listeCoul.index(item.color)  # Couleur présente dans la liste ?
            except ValueError:
                listeCoul.append(item.color)  # Si non , alors ajout de la couleur à la liste

        return listeCoul


def chargerBench(fileName):
    """Lit un bench et retourne une liste d'objets et de boites."""
    with open(fileName, "r") as bench:
        listItem = []
        capBox = []

        donneesBoite = bench.readline().split(' ')
        donneesBoite[-1] = donneesBoite[-1].replace('\n',
                                                    '')  # Suppression du retour à la ligne pour le dernier élément
        # de la liste
        nbTypesBoites = int(donneesBoite[0])
        for i in range(0, nbTypesBoites):
            capBox.append(int(donneesBoite[i + 1]))

        nbCouleurs = int(bench.readline().replace('\n', ''))
        nbObjects = int(bench.readline().replace('\n', ''))

        for i in range(0, nbObjects):
            donneesObjet = bench.readline().split('\t')
            donneesObjet[-1] = donneesObjet[-1].replace('\n',
                                                        '')  # Suppression du retour à la ligne pour le dernier
            # élément de la liste
            listItem.append(Item(int(donneesObjet[0]), int(donneesObjet[1]), i))

    return capBox, listItem


def loadBenchFromFile(fileName):
    with open(fileName, "r") as bench:
        listItem = []
        listCap = []
        benchArray = bench.readline().split(' ')
        benchArray[-1] = benchArray[-1].replace('\n', '')
        for i in range(1, len(benchArray)):
            listCap.append(benchArray[i])
        nbColor = bench.readline()
        nbObject = bench.readline()
        for i in range(0, int(nbObject)):
            benchObjArray = bench.readline().split("\t")
            benchObjArray[-1] = benchObjArray[-1].replace('\n', '')
            listItem.append(Item(benchObjArray[0], benchObjArray[1], i))
        return listItem, listCap


def printBoxStatus(boxList):
    totalCap = 0
    for item in boxList:
        print("Boite {}".format(item.id))
        percent = ((int(item.cap) - int(item.capResiduelle())) * 10) / int(item.cap)
        strStar = ""
        for i in range(10):
            if i > round(percent):
                strStar += " - "
            else:
                strStar += " * "
        print("[{}] remplie à {:.0f} %\n".format(strStar, percent*10))
        strStar = ""
        totalCap += item.capResiduelle()
    print("Total perte = {:.2f} %\n".format(totalCap / len(boxList)))


if __name__ == '__main__':
    obj = Item(20, 0, 1)
    obj2 = Item(30, 1, 2)
    obj3 = Item(5, 4, 3)
    b = Box(60, 4)
    b.addItem(obj)
    b.addItem(obj2)
    b.addItem(obj3)
    print(b)
