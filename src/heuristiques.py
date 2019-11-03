import random
from time import clock

from classes import Boite , Objet , chargerBench


def permuter_objets(boite1 , boite2 , obj1 , obj2):
    """Permute 2 objets entre 2 boites. Attention , il faut que les contraintes de poids et de couleur
    soient toujours respectés."""
    boite1.supprimerObjet(obj1)
    boite2.supprimerObjet(obj2)
    
    if (boite1.ajouterObjet(obj2) == False):
        boite1.ajouterObjet(obj1)
        boite2.ajouterObjet(obj2)
    elif (boite2.ajouterObjet(obj1) == False):
        boite1.supprimerObjet(obj2)
        boite1.ajouterObjet(obj1)
        boite2.ajouterObjet(obj2)

def objet_le_plus_lourd(listeObj):
    """Retourne l'objet de poids le plus élevé parmi la liste d'objets."""
    objSelecetionne = listeObj[0]
    for obj in listeObj:
        if obj.poids > objSelecetionne.poids:
            objSelecetionne = obj
    
    return objSelecetionne

def cap_la_plus_proche(poids ,listeCap):
    listeCap2 = listeCap.copy()
    for cap in listeCap2:
        cap -= poids
        if cap >= 0:
            return(cap + poids)
    return listeCap[-1]
    

def trier_objets_selon_poids(listeObj):
    """Trie dans l'ordre décroissant selon leurs poids une liste d'objets."""
    listeObj2 = listeObj.copy()
    nouvListe = []
    while listeObj2 != []:
        obj = objet_le_plus_lourd(listeObj2)
        nouvListe.append(obj)
        listeObj2.remove(obj)
    return nouvListe
    
    
    

def heur_naive(listeObj , capBoites):
    """Heuristique naive. On place tous les objets dans toutes les boites."""
    listeBoites = []
    listeObj2 = listeObj.copy() # Copie de la liste d'objets afin de ne pas altérer la liste originale
    i = 0 # itérateur pour l'id des boites
    
    for obj in listeObj2:
        try:
            capBoites.index(obj.poids) # Si le poids de l'objet coincide avce la capacité d'une boite
            boite = Boite(obj.poids,i) # Création de la boite appropriée
            boite.ajouterObjet(obj) # Ajout de l'objet à cette boite
            listeBoites.append(boite) # Ajout de la boite à la liste des boites
            i += 1
        except ValueError:
            pass
        
    for boite in listeBoites: # Suppression des objets déjà rangés dans des boites
        for obj in boite.listeObj:
            listeObj2.remove(obj)
    
    while listeObj2 != []:
        sumPoids = 0 # Somme des poids des objets non rangés
        for obj in listeObj2:
            sumPoids += obj.poids
        capBoite = cap_la_plus_proche(sumPoids, capBoites)
        boite = Boite(capBoite , i) # Création d'un boite avec la cap. la plus proche de la somme des poids des objets
        i += 1
        for obj in listeObj2:
            boite.ajouterObjet(obj) # Ajout des objets restants dans la boite (risque de rejet d'objets à cause de la contrainte de couleurs)
        sumPoids = 0 # Somme des poids des objets dans la boite
        for obj in boite.listeObj:
            sumPoids += obj.poids
        boite.cap = cap_la_plus_proche(sumPoids, capBoites) # Réadaptation de la capacité de la boite
        for obj in boite.listeObj: # Suppression des objets déjà rangés dans des boites
            listeObj2.remove(obj)
        listeBoites.append(boite) # Ajout de la boite à la liste des boites
        
    sumCapResid = 0
    for boite in listeBoites:
        sumCapResid += boite.capResiduelle()
        
    return (listeBoites , sumCapResid)
    
def heur_naive_bis(listeObj , capBoites):
    """Même heuristique que précédemment sauf que l'étape de placer les objets de taille égale à un capacité d'une boite ; a été retirée."""
    listeBoites = []
    listeObj2 = listeObj.copy() # Copie de la liste d'objets afin de ne pas altérer la liste originale
    i = 0 # itérateur pour l'id des boites
    
    while listeObj2 != []:
        sumPoids = 0 # Somme des poids des objets non rangés
        for obj in listeObj2:
            sumPoids += obj.poids
        capBoite = cap_la_plus_proche(sumPoids, capBoites)
        boite = Boite(capBoite , i) # Création d'un boite avec la cap. la plus proche de la somme des poids des objets
        i += 1
        for obj in listeObj2:
            boite.ajouterObjet(obj) # Ajout des objets restants dans la boite (risque de rejet d'objets à cause de la contrainte de couleurs)
        sumPoids = 0 # Somme des poids des objets dans la boite
        for obj in boite.listeObj:
            sumPoids += obj.poids
        boite.cap = cap_la_plus_proche(sumPoids, capBoites) # Réadaptation de la capacité de la boite
        for obj in boite.listeObj: # Suppression des objets déjà rangés dans des boites
            listeObj2.remove(obj)
        listeBoites.append(boite) # Ajout de la boite à la liste des boites
        
    sumCapResid = 0
    for boite in listeBoites:
        sumCapResid += boite.capResiduelle()
        
    return (listeBoites , sumCapResid)
        
def heur_naive_trie_selon_poids(listeObj , capBoites):
    """Même heuristique que précédemment sauf que l'étape de placer les objets de taille égale à un capacité d'une boite ; a été retirée
    et les objets sont triés selon leur poids par ordre décroissant."""
    listeBoites = []
    listeObj2 = listeObj.copy() # Copie de la liste d'objets afin de ne pas altérer la liste originale
    i = 0 # itérateur pour l'id des boites
    listeObj2 = trier_objets_selon_poids(listeObj2)
    while listeObj2 != []:
        sumPoids = 0 # Somme des poids des objets non rangés
        for obj in listeObj2:
            sumPoids += obj.poids
        capBoite = cap_la_plus_proche(sumPoids, capBoites)
        boite = Boite(capBoite , i) # Création d'un boite avec la cap. la plus proche de la somme des poids des objets
        i += 1
        for obj in listeObj2:
            boite.ajouterObjet(obj) # Ajout des objets restants dans la boite (risque de rejet d'objets à cause de la contrainte de couleurs)
        sumPoids = 0 # Somme des poids des objets dans la boite
        for obj in boite.listeObj:
            sumPoids += obj.poids
        boite.cap = cap_la_plus_proche(sumPoids, capBoites) # Réadaptation de la capacité de la boite
        for obj in boite.listeObj: # Suppression des objets déjà rangés dans des boites
            listeObj2.remove(obj)
        listeBoites.append(boite) # Ajout de la boite à la liste des boites
        
    sumCapResid = 0
    for boite in listeBoites:
        sumCapResid += boite.capResiduelle()
        
    return (listeBoites , sumCapResid)
        
def heur_naive_trie_selon_poids_depl_obj(listeObj , capBoites , tempsLimite=1):
    """Même heuristique que précédemment sauf que l'étape de placer les objets de taille égale à un capacité d'une boite ; a été retirée
    et les objets sont triés selon leur poids par ordre décroissant.
    Ensuite on essaie de transférer des objets dans des boites qui pourraient être comblées par ces objets là.
    Et on redimensionne (si possible) la boite à qui on a volé un objet par un des types de boites existants afin de réduire la 
    capacité perdue. La limite de temps est en secondes. (par défaut = 1 seconde)"""
    
    tempsDebut = clock()
    
    listeBoites = []
    listeObj2 = listeObj.copy() # Copie de la liste d'objets afin de ne pas altérer la liste originale
    i = 0 # itérateur pour l'id des boites
    listeObj2 = trier_objets_selon_poids(listeObj2)
    while listeObj2 != []:
        sumPoids = 0 # Somme des poids des objets non rangés
        for obj in listeObj2:
            sumPoids += obj.poids
        capBoite = cap_la_plus_proche(sumPoids, capBoites)
        boite = Boite(capBoite , i) # Création d'un boite avec la cap. la plus proche de la somme des poids des objets
        i += 1
        for obj in listeObj2:
            boite.ajouterObjet(obj) # Ajout des objets restants dans la boite (risque de rejet d'objets à cause de la contrainte de couleurs)
        sumPoids = 0 # Somme des poids des objets dans la boite
        for obj in boite.listeObj:
            sumPoids += obj.poids
        boite.cap = cap_la_plus_proche(sumPoids, capBoites) # Réadaptation de la capacité de la boite
        for obj in boite.listeObj: # Suppression des objets déjà rangés dans des boites
            listeObj2.remove(obj)
        listeBoites.append(boite) # Ajout de la boite à la liste des boites
        
    sumCapResid = 0
    for boite in listeBoites:
        sumCapResid += boite.capResiduelle()
    
    tempsActuel = clock()
    
    # Exploration du voisinage de la solution que l'on vient de trouver
    while ((tempsActuel - tempsDebut) < tempsLimite) and (sumCapResid > 0):
        # boucle qui s'arrêtera lortsque la limite de temps sera dépassée
        boiteLaPlusVide = listeBoites[0]
        for boite in listeBoites: # Sélection de la boite la plus vide
            if boiteLaPlusVide.capResiduelle() < boite.capResiduelle():
                boiteLaPlusVide = boite  
        for boite in listeBoites:
            for obj in boite.listeObj:
                if obj.poids == boiteLaPlusVide.capResiduelle() and (boite != boiteLaPlusVide): # On cherche un objet qui pourrait remplir au maximum la boite la plus vide
                    if boiteLaPlusVide.ajouterObjet(obj) == True: # Ajout de l'objet avec succès ?
                        boite.supprimerObjet(obj.id) # La boite donne son objet à la boite la plus vide
                        sumPoids = 0 # Somme des poids des objets dans la boite
                        for obj in boite.listeObj:
                            sumPoids += obj.poids
                        boite.cap = cap_la_plus_proche(sumPoids, capBoites) # Réadaptation de la capacité de la boite à qui on a pris un objet
        tempsActuel = clock()
        sumCapResid = 0
        for boite in listeBoites:
            sumCapResid += boite.capResiduelle()
                        
                        
                    
        
            
        
    
        
    return (listeBoites , sumCapResid)

        
def heur_naive_trie_selon_poids_depl_obj_bis(listeObj , capBoites , tempsLimite=1):
    """Même heuristique que précédemment sauf que l'étape de placer les objets de taille égale à un capacité d'une boite ; a été remise ici
    et les objets sont triés selon leur poids par ordre décroissant.
    Ensuite on essaie de transférer des objets dans des boites qui pourraient être comblées par ces objets là.
    Et on redimensionne (si possible) la boite à qui on a volé un objet par un des types de boites existants afin de réduire la 
    capacité perdue. La limite de temps est en secondes. (par défaut = 1 seconde)"""
    
    tempsDebut = clock()
    
    listeBoites = []
    listeObj2 = listeObj.copy() # Copie de la liste d'objets afin de ne pas altérer la liste originale
    i = 0 # itérateur pour l'id des boites
    listeObj2 = trier_objets_selon_poids(listeObj2)
    
    # L'étape de placer des objets qui sont égaux à une capacité de boite donné a été rétablie dans cette heuristique.
    for obj in listeObj2:
        try:
            capBoites.index(obj.poids) # Si le poids de l'objet coincide avce la capacité d'une boite
            boite = Boite(obj.poids,i) # Création de la boite appropriée
            boite.ajouterObjet(obj) # Ajout de l'objet à cette boite
            listeBoites.append(boite) # Ajout de la boite à la liste des boites
            i += 1
        except ValueError:
            pass
        
    for boite in listeBoites: # Suppression des objets déjà rangés dans des boites
        for obj in boite.listeObj:
            listeObj2.remove(obj)
    
     
    while listeObj2 != []:
        sumPoids = 0 # Somme des poids des objets non rangés
        for obj in listeObj2:
            sumPoids += obj.poids
        capBoite = cap_la_plus_proche(sumPoids, capBoites)
        boite = Boite(capBoite , i) # Création d'un boite avec la cap. la plus proche de la somme des poids des objets
        i += 1
        for obj in listeObj2:
            boite.ajouterObjet(obj) # Ajout des objets restants dans la boite (risque de rejet d'objets à cause de la contrainte de couleurs)
        sumPoids = 0 # Somme des poids des objets dans la boite
        for obj in boite.listeObj:
            sumPoids += obj.poids
        boite.cap = cap_la_plus_proche(sumPoids, capBoites) # Réadaptation de la capacité de la boite
        for obj in boite.listeObj: # Suppression des objets déjà rangés dans des boites
            listeObj2.remove(obj)
        listeBoites.append(boite) # Ajout de la boite à la liste des boites
        
    sumCapResid = 0
    for boite in listeBoites:
        sumCapResid += boite.capResiduelle()
    
    tempsActuel = clock()
    while ((tempsActuel - tempsDebut) < tempsLimite) and (sumCapResid > 0):
        # boucle qui s'arrêtera lortsque la limite de temps sera dépassée
        boiteLaPlusVide = listeBoites[0]
        for boite in listeBoites: # Sélection de la boite la plus vide
            if boiteLaPlusVide.capResiduelle() < boite.capResiduelle():
                boiteLaPlusVide = boite  
        for boite in listeBoites:
            for obj in boite.listeObj:
                if obj.poids <= boiteLaPlusVide.capResiduelle() and (boite != boiteLaPlusVide): # On cherche un objet qui pourrait remplir au maximum la boite la plus vide
                    if boiteLaPlusVide.ajouterObjet(obj) == True: # Ajout de l'objet avec succès ?
                        boite.supprimerObjet(obj.id) # La boite donne son objet à la boite la plus vide
                        sumPoids = 0 # Somme des poids des objets dans la boite
                        for obj in boite.listeObj:
                            sumPoids += obj.poids
                        boite.cap = cap_la_plus_proche(sumPoids, capBoites) # Réadaptation de la capacité de la boite
        tempsActuel = clock()
        sumCapResid = 0
        for boite in listeBoites:
            sumCapResid += boite.capResiduelle()
                        
                        
                    
        
            
        
    
        
    return (listeBoites , sumCapResid)

def heur_naive_trie_selon_poids_depl_obj_ter(listeObj , capBoites , tempsLimite=1):
    """Même heuristique que précédemment sauf que l'étape de placer les objets de taille égale à un capacité d'une boite ; a été remise ici
    et les objets sont triés selon leur poids par ordre décroissant.
    Ensuite on essaie de transférer des objets dans des boites qui pourraient être comblées par ces objets là.
    Et on redimensionne (si possible) la boite à qui on a volé un objet par un des types de boites existants afin de réduire la 
    capacité perdue. La limite de temps est en secondes. (par défaut = 1 seconde)"""
    
    tempsDebut = clock()
    
    listeBoites = []
    listeObj2 = listeObj.copy() # Copie de la liste d'objets afin de ne pas altérer la liste originale
    i = 0 # itérateur pour l'id des boites
    listeObj2 = trier_objets_selon_poids(listeObj2)
    
    # L'étape de placer des objets qui sont égaux à une capacité de boite donné a été rétablie dans cette heuristique.
    for obj in listeObj2:
        try:
            capBoites.index(obj.poids) # Si le poids de l'objet coincide avce la capacité d'une boite
            boite = Boite(obj.poids,i) # Création de la boite appropriée
            boite.ajouterObjet(obj) # Ajout de l'objet à cette boite
            listeBoites.append(boite) # Ajout de la boite à la liste des boites
            i += 1
        except ValueError:
            pass
        
    for boite in listeBoites: # Suppression des objets déjà rangés dans des boites
        for obj in boite.listeObj:
            listeObj2.remove(obj)
    
     
    while listeObj2 != []:
        sumPoids = 0 # Somme des poids des objets non rangés
        for obj in listeObj2:
            sumPoids += obj.poids
        capBoite = cap_la_plus_proche(sumPoids, capBoites)
        boite = Boite(capBoite , i) # Création d'un boite avec la cap. la plus proche de la somme des poids des objets
        i += 1
        for obj in listeObj2:
            boite.ajouterObjet(obj) # Ajout des objets restants dans la boite (risque de rejet d'objets à cause de la contrainte de couleurs)
        sumPoids = 0 # Somme des poids des objets dans la boite
        for obj in boite.listeObj:
            sumPoids += obj.poids
        boite.cap = cap_la_plus_proche(sumPoids, capBoites) # Réadaptation de la capacité de la boite
        for obj in boite.listeObj: # Suppression des objets déjà rangés dans des boites
            listeObj2.remove(obj)
        listeBoites.append(boite) # Ajout de la boite à la liste des boites
        
    sumCapResid = 0
    for boite in listeBoites:
        sumCapResid += boite.capResiduelle()
    
    tempsActuel = clock()
    while ((tempsActuel - tempsDebut) < tempsLimite) and (sumCapResid > 0):
        # boucle qui s'arrêtera lortsque la limite de temps sera dépassée
        boiteLaPlusVide = listeBoites[0]
        for boite in listeBoites: # Sélection de la boite la plus vide
            if boiteLaPlusVide.capResiduelle() < boite.capResiduelle():
                boiteLaPlusVide = boite  
        objetsCandidats = []
        for boite in listeBoites:
            for obj in boite.listeObj: # Recherche des objets candidats pouvant rentrer dans la boite vide
                if obj.poids <= boiteLaPlusVide.capResiduelle() and boite != boiteLaPlusVide:
                    objetsCandidats.append(obj)
        objetsCandidats = trier_objets_selon_poids(objetsCandidats) # Tri de ces objets par ordre décroissnt de poids
        objAjoute = None
        for obj in objetsCandidats: # Tentative d'ajout d'un de ces objets dans la boite la plus vide
            if boiteLaPlusVide.ajouterObjet(obj) == True:
                objAjoute = obj
                break # Sortie de la boucle for
        if objAjoute != None:
            for boite in listeBoites:
                try:
                    boite.listeObj.index(obj) # Est-ce que l'objet ajouté vient de cette boite ?
                    for obj in boite.listeObj:
                        sumPoids += obj.poids
                    boite.cap = cap_la_plus_proche(sumPoids, capBoites) # Si oui , Réadaptation de la capacité de la boite
                except ValueError:
                    pass
        tempsActuel = clock()
        sumCapResid = 0
        for boite in listeBoites:
            sumCapResid += boite.capResiduelle()
                        
                        
                    
        
            
        
    
        
    return (listeBoites , sumCapResid)
    
          
if __name__ == '__main__':
    capBoites , listeObj = chargerBench("../instances2/bench_20_10")
    boites1 , capPerdue1 = heur_naive_trie_selon_poids_depl_obj_bis(listeObj, capBoites)
    print("Capacité perdue = " + str(capPerdue1))
    for boite in boites1:
        print(boite)


    
    
    
    

