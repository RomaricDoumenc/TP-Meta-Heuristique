import random
from time import clock
import pdb
import math

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

def trier_objets_aleatoire(listeObj):
    """Trie les objets de manière aléatoire (au hasard)."""
    listeObj2 = listeObj.copy()
    nouvListe = []
    while listeObj2 != []:
        obj = listeObj2[random.randrange(len(listeObj2))] # Sélection d'un objet au hasars dans la listeObj2
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
 
        #pdb.set_trace()  
        objetsCandidats = []
        for boite in listeBoites:
            for obj in boite.listeObj: # Recherche des objets candidats pouvant rentrer dans la boite vide
                if obj.poids <= boiteLaPlusVide.capResiduelle() and boite != boiteLaPlusVide:
                    objetsCandidats.append(obj)
        objetsCandidats = trier_objets_selon_poids(objetsCandidats) # Tri de ces objets par ordre décroissnt de poids
        objAjoute = None
        for obj in objetsCandidats: # Tentative d'ajout d'un de ces objets dans la boite la plus vide
            boiteOriginelle = obj.boite # Boite originelle d'où provient l'objet candidat 
            if boiteLaPlusVide.ajouterObjet(obj) == True:
                objAjoute = obj
                boiteOriginelle.supprimerObjet(obj.id)
                sumPoids = 0 # Somme des poids des objets dans la boite
                for o in boiteOriginelle.listeObj:
                    sumPoids += o.poids
                boiteOriginelle.cap = cap_la_plus_proche(sumPoids, capBoites) # Réadaptation de la capacité de la boite
                """ print(boiteOriginelle)
                pdb.set_trace() """
                #break # Sortie de la boucle for
        tempsActuel = clock()
        sumCapResid = 0
        for boite in listeBoites:
            sumCapResid += boite.capResiduelle()
            #print(boite)
        #pdb.set_trace()
                        
                        
                    
        
            
        
    
        
    return (listeBoites , sumCapResid)
    
def heur_naive_trie_selon_poids_depl_obj_alea(listeObj , capBoites , tempsLimite=1e-6):
    """Même heuristique que précédemment sauf que l'étape de placer les objets de taille égale à un capacité d'une boite ; a été remise ici
    et les objets sont triés de manière aléatoire.
    Ensuite on essaie de transférer des objets dans des boites qui pourraient être comblées par ces objets là.
    Et on redimensionne (si possible) la boite à qui on a volé un objet par un des types de boites existants afin de réduire la 
    capacité perdue. La limite de temps est en secondes. (par défaut = 1 microseconde)"""
    
    tempsDebut = clock()
    
    listeBoites = []
    listeObj2 = listeObj.copy() # Copie de la liste d'objets afin de ne pas altérer la liste originale
    i = 0 # itérateur pour l'id des boites
    listeObj2 = trier_objets_aleatoire(listeObj2)
    
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
 
        #pdb.set_trace()  
        objetsCandidats = []
        for boite in listeBoites:
            for obj in boite.listeObj: # Recherche des objets candidats pouvant rentrer dans la boite vide
                if obj.poids <= boiteLaPlusVide.capResiduelle() and boite != boiteLaPlusVide:
                    objetsCandidats.append(obj)
        objetsCandidats = trier_objets_selon_poids(objetsCandidats) # Tri de ces objets par ordre décroissnt de poids
        objAjoute = None
        for obj in objetsCandidats: # Tentative d'ajout d'un de ces objets dans la boite la plus vide
            boiteOriginelle = obj.boite # Boite originelle d'où provient l'objet candidat 
            if boiteLaPlusVide.ajouterObjet(obj) == True:
                objAjoute = obj
                boiteOriginelle.supprimerObjet(obj.id)
                sumPoids = 0 # Somme des poids des objets dans la boite
                for o in boiteOriginelle.listeObj:
                    sumPoids += o.poids
                boiteOriginelle.cap = cap_la_plus_proche(sumPoids, capBoites) # Réadaptation de la capacité de la boite
                """ print(boiteOriginelle)
                pdb.set_trace() """
                #break # Sortie de la boucle for
        tempsActuel = clock()
        sumCapResid = 0
        for boite in listeBoites:
            sumCapResid += boite.capResiduelle()
            #print(boite)
        #pdb.set_trace()
                        
                        
                    
        
            
        
    
        
    return (listeBoites , sumCapResid)
    
def repeter_heur_alea(listeObj , capBoites , nbExperiences=1000):
    """On répète un grand nombre de fois l'heuristique précédente car l'aléatoire peut donner des solutions très mal optimisées.
    Le but est de varier le plus possible les solutions initiales afin de maximiser l'espace de recherche. 
    Et à la fin on prendra la meilleure solution x."""
    meilleurX = None
    meilleurF_X = math.inf
    tempsDebut = clock()
    for i in range(nbExperiences):
        x , f_x = heur_naive_trie_selon_poids_depl_obj_alea(listeObj,capBoites)
        if f_x < meilleurF_X:
            meilleurX = x
            meilleurF_X = f_x
        tempsActuel = clock()
        if tempsActuel - tempsDebut >= 60 or meilleurF_X <= 0: # Limite de 1 minute par bench dépassé ou optimum global trouvé ?
            break # On arrête la recherche
    return meilleurX , meilleurF_X

def heur_naive_trie_selon_poids_depl_obj_quad(listeObj , capBoites , tempsLimite=1):
    """Même heuristique que précédemment sauf que l'étape de placer les objets PAR 2 de taille égale à un capacité d'une boite ; a été remise ici
    et les objets sont triés selon leur poids par ordre décroissant.
    Ensuite on essaie de transférer des objets dans des boites qui pourraient être comblées par ces objets là.
    Et on redimensionne (si possible) la boite à qui on a volé un objet par un des types de boites existants afin de réduire la 
    capacité perdue. La limite de temps est en secondes. (par défaut = 1 seconde)"""
    
    tempsDebut = clock()
    
    listeBoites = []
    listeObj2 = listeObj.copy() # Copie de la liste d'objets afin de ne pas altérer la liste originale
    i = 0 # itérateur pour l'id des boites
    listeObj2 = trier_objets_selon_poids(listeObj2)
    couplesPossibles = []
    
    # On prend les couples d'objets qui pourraient remplir au maximum un type de boite.
    for obj1 in listeObj2:
        for obj2 in listeObj2:
            if obj1 != obj2:
                try:
                    capBoites.index(obj1.poids + obj2.poids) # Est-ce que le couple actuel d'objets peut remplir au maximum un type de boite ?
                    couplesPossibles.append((obj1,obj2))
                except ValueError:
                    pass
    
    for obj1,obj2 in couplesPossibles:
        try:
            listeObj2.index(obj1) # Est-ce que les 2 objets ne sont pas rangés ?
            listeObj2.index(obj2)
            boite = Boite(obj1.poids + obj2.poids , i)
            boite.ajouterObjet(obj1)
            boite.ajouterObjet(obj2)
            listeObj2.remove(obj1)
            listeObj2.remove(obj2)
            listeBoites.append(boite)
            i += 1
        except ValueError:
            pass
    
     
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
 
        #pdb.set_trace()  
        objetsCandidats = []
        for boite in listeBoites:
            for obj in boite.listeObj: # Recherche des objets candidats pouvant rentrer dans la boite vide
                if obj.poids <= boiteLaPlusVide.capResiduelle() and boite != boiteLaPlusVide:
                    objetsCandidats.append(obj)
        objetsCandidats = trier_objets_selon_poids(objetsCandidats) # Tri de ces objets par ordre décroissnt de poids
        objAjoute = None
        for obj in objetsCandidats: # Tentative d'ajout d'un de ces objets dans la boite la plus vide
            boiteOriginelle = obj.boite # Boite originelle d'où provient l'objet candidat 
            if boiteLaPlusVide.ajouterObjet(obj) == True:
                objAjoute = obj
                boiteOriginelle.supprimerObjet(obj.id)
                sumPoids = 0 # Somme des poids des objets dans la boite
                for o in boiteOriginelle.listeObj:
                    sumPoids += o.poids
                boiteOriginelle.cap = cap_la_plus_proche(sumPoids, capBoites) # Réadaptation de la capacité de la boite
                """ print(boiteOriginelle)
                pdb.set_trace() """
                #break # Sortie de la boucle for
        tempsActuel = clock()
        sumCapResid = 0
        for boite in listeBoites:
            sumCapResid += boite.capResiduelle()
            #print(boite)
        #pdb.set_trace()
                        
                        
                    
        
            
        
    
        
    return (listeBoites , sumCapResid)
    
def heur_naive_trie_selon_poids_depl_obj_quad_alea(listeObj , capBoites , tempsLimite=1):
    """Même heuristique que précédemment sauf que l'étape de placer les objets PAR 2 de taille égale à un capacité d'une boite ; a été remise ici
    et les objets sont triés selon leur poids par ordre décroissant.
    Ensuite on essaie de transférer des objets dans des boites qui pourraient être comblées par ces objets là.
    Et on redimensionne (si possible) la boite à qui on a volé un objet par un des types de boites existants afin de réduire la 
    capacité perdue. La limite de temps est en secondes. (par défaut = 1 seconde)"""
    
    tempsDebut = clock()
    
    listeBoites = []
    listeObj2 = listeObj.copy() # Copie de la liste d'objets afin de ne pas altérer la liste originale
    i = 0 # itérateur pour l'id des boites
    listeObj2 = trier_objets_aleatoire(listeObj2)
    couplesPossibles = []
    
    # On prend les couples d'objets qui pourraient remplir au maximum un type de boite.
    for obj1 in listeObj2:
        for obj2 in listeObj2:
            if obj1 != obj2:
                try:
                    capBoites.index(obj1.poids + obj2.poids) # Est-ce que le couple actuel d'objets peut remplir au maximum un type de boite ?
                    couplesPossibles.append((obj1,obj2))
                except ValueError:
                    pass
    
    for obj1,obj2 in couplesPossibles:
        try:
            listeObj2.index(obj1) # Est-ce que les 2 objets ne sont pas rangés ?
            listeObj2.index(obj2)
            boite = Boite(obj1.poids + obj2.poids , i)
            boite.ajouterObjet(obj1)
            boite.ajouterObjet(obj2)
            listeObj2.remove(obj1)
            listeObj2.remove(obj2)
            listeBoites.append(boite)
            i += 1
        except ValueError:
            pass
    
     
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
 
        #pdb.set_trace()  
        objetsCandidats = []
        for boite in listeBoites:
            for obj in boite.listeObj: # Recherche des objets candidats pouvant rentrer dans la boite vide
                if obj.poids <= boiteLaPlusVide.capResiduelle() and boite != boiteLaPlusVide:
                    objetsCandidats.append(obj)
        objetsCandidats = trier_objets_selon_poids(objetsCandidats) # Tri de ces objets par ordre décroissnt de poids
        objAjoute = None
        for obj in objetsCandidats: # Tentative d'ajout d'un de ces objets dans la boite la plus vide
            boiteOriginelle = obj.boite # Boite originelle d'où provient l'objet candidat 
            if boiteLaPlusVide.ajouterObjet(obj) == True:
                objAjoute = obj
                boiteOriginelle.supprimerObjet(obj.id)
                sumPoids = 0 # Somme des poids des objets dans la boite
                for o in boiteOriginelle.listeObj:
                    sumPoids += o.poids
                boiteOriginelle.cap = cap_la_plus_proche(sumPoids, capBoites) # Réadaptation de la capacité de la boite
                """ print(boiteOriginelle)
                pdb.set_trace() """
                #break # Sortie de la boucle for
        tempsActuel = clock()
        sumCapResid = 0
        for boite in listeBoites:
            sumCapResid += boite.capResiduelle()
            #print(boite)
        #pdb.set_trace()
                        
                        
                    
        
            
        
    
        
    return (listeBoites , sumCapResid)
    
def repeter_heur_alea2(listeObj , capBoites , nbExperiences=1000):
    """On répète un grand nombre de fois l'heuristique précédente car l'aléatoire peut donner des solutions très mal optimisées.
    Le but est de varier le plus possible les solutions initiales afin de maximiser l'espace de recherche. 
    Et à la fin on prendra la meilleure solution x."""
    meilleurX = None
    meilleurF_X = math.inf
    tempsDebut = clock()
    for i in range(nbExperiences):
        print("iter = " + str(i + 1) + " : " + str(meilleurF_X))
        x , f_x = heur_naive_trie_selon_poids_depl_obj_quad_alea(listeObj,capBoites)
        if f_x < meilleurF_X:
            meilleurX = x
            meilleurF_X = f_x
        tempsActuel = clock()
        if tempsActuel - tempsDebut >= 60 or meilleurF_X <= 0: # Limite de 1 minute par bench dépassé ?
            break # On arrête la recherche
    return meilleurX , meilleurF_X


if __name__ == '__main__':
    capBoites , listeObj = chargerBench("../instances2/bench_2_1")
    boites1 , capPerdue1 = repeter_heur_alea2(listeObj, capBoites)
    for boite in boites1:
        print(boite)
    print("Capacité perdue = " + str(capPerdue1))


    
    
    
    

