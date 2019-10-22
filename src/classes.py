
class Objet():
    def __init__(self , poids , color , idObj):
        self.poids = poids
        self.color = color
        self.id = idObj
                
    def __str__(self):
        return ("[Objet {} : Poids = {} , Couleur = {}]".format(self.id,self.poids,self.color))
    
           
        
class Boite():
    def __init__(self , cap , idBoite):
        self.listeObj = []
        self.cap = cap
        self.id = idBoite
    
    def capResiduelle(self):
        """Capacité restante dans la boite."""
        capResid = self.cap
        for obj in self.listeObj:
            capResid -= obj.poids
        return capResid
        
    def ajouterObjet(self , obj):
        """Ajoute un objet dans la boite s'il reste suffisamment de place et si 
        la contrainte de 2 couleurs maximum est respectée."""
        
        if self.capResiduelle() - obj.poids < 0:
            #print("Impossible d'ajouter l'objet " + str(obj) + " : pas assez de place dans la boite.")
            return False
        
        listeCoul = self.listeCouleurs()
        
        if len(listeCoul) >= 2:
            try:
                listeCoul.index(obj.color)
            except ValueError:
                #print("Impossible d'ajouter l'objet " + str(obj) + " : 2 couleurs maximum.")
                return False  
                
        self.listeObj.append(obj)
        
        return True
    
    def supprimerObjet(self , idObj):
        """Supprime un objet selon son id."""
        for obj in self.listeObj:
            if obj.id == idObj:
                self.listeObj.remove(obj)
                return True
        return False
        
            
        
    def __str__(self):
        chaine = 'Boite {} '.format(self.id)
        for obj in self.listeObj:
            chaine += str(obj) + " ; "
        chaine += "Capacité restante = " +  str(self.capResiduelle())
        return chaine
        
    def listeCouleurs(self):
        """Retourne le nombre de couleurs différentes des objets de la boite."""
        listeCoul = []
        for obj in self.listeObj:
            try:
                listeCoul.index(obj.color) # Couleur présente dans la liste ?
            except ValueError:
                listeCoul.append(obj.color) # Si non , alors ajout de la couleur à la liste
                
        return listeCoul              
        


def chargerBench(nomFichier):
    """Lit un bench et retourne une liste d'objets et de boites."""
    with open(nomFichier , "r") as bench:
        listeObjets = []
        capBoites = []
        
        donneesBoite = bench.readline().split(' ')
        donneesBoite[-1] = donneesBoite[-1].replace('\n','') # Suppression du retour à la ligne pour le dernier élément de la liste
        nbTypesBoites = int(donneesBoite[0])
        for i in range(0,nbTypesBoites):
            capBoites.append(int(donneesBoite[i+1]))
            
            
        nbCouleurs = int(bench.readline().replace('\n',''))
        nbObjets = int(bench.readline().replace('\n',''))
        
        for i in range(0,nbObjets):
            donneesObjet = bench.readline()
            if donneesObjet == "13      58\n": # Rectification d'une erreur de formatage récurrente sur tous les benchs
                donneesObjet = "13\t58"
            donneesObjet = donneesObjet.split('\t')
            donneesObjet[-1] = donneesObjet[-1].replace('\n','') # Suppression du retour à la ligne pour le dernier élément de la liste
            listeObjets.append(Objet(int(donneesObjet[0]) , int(donneesObjet[1]) , i))
            
                        
    return (capBoites , listeObjets)



if __name__ == '__main__':
    obj = Objet(20,0,1)
    obj2 = Objet(30,1,2)
    obj3 = Objet(5,4,3)
    b = Boite(60,4)
    b.ajouterObjet(obj)
    b.ajouterObjet(obj2)
    b.ajouterObjet(obj3)
    print(b)