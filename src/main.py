from heuristiques import *
from time import perf_counter
from classes import Objet , Boite , chargerBench , genererBenchAleatoire
import sys

"""
    Pour tester un bench , placez-vous dans un terminal , placez-vous dans le dossier src
    où est contenu ce main et tapez la commande : python3 main.py nom_du_bench 
    où nom_du_bench est le chemin relatif (ou absolu) vers le bench que vous souhaitez tester.
"""

if __name__ == "__main__":
    # nomFichier = input("Chemin relatif ou absolu du bench que vous souhaitez tester : ")
    nbIterations = int(input("Nombre d'itérations : "))
    capBoites,listeObj = genererBenchAleatoire(
        nbObjets = 250,
        nbTypes = 10,
        nbCouleurs = 30
    )
    debut = perf_counter()
    boites , capPerdue = repeter_heur_alea2(listeObj, capBoites, nbExperiences=nbIterations)
    fin = perf_counter()
   
    for boite in boites:
        print(boite)
    print("\nCapacité perdue heur_alea2 = " + str(capPerdue))
    print("Exécute en {} secondes.".format(fin-debut))
