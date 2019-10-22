from classes import Boite , Objet , chargerBench
import random

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
        
        
    

        
        



    
    
    
    
    #===========================================================================
    # for obj in listeObj:
    #     print(obj)
    # 
    # for boite in boites:
    #     print(boite)
    #     
    #===========================================================================
