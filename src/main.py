from heuristiques import *
from classes import Objet , Boite , chargerBench
import sys

"""
    Pour tester un bench , placez-vous dans un terminal , placez-vous dans le dossier src
    où est contenu ce main et tapez la commande : python3 main.py nom_du_bench 
    où nom_du_bench est le chemin relatif (ou absolu) vers le bench que vous souhaitez tester.
"""

if __name__ == "__main__":
    nomFichier = input("Chemin relatif ou absolu du bench que vous souhaitez tester : ")
    capBoites,listeObj = chargerBench(nomFichier) # Récupération de l'argument n°2 qui correspond au bench passé en parammètre
    boites1 , capPerdue1 = heur_naive(listeObj, capBoites)
    boites2 , capPerdue2 = heur_naive_bis(listeObj, capBoites)
    boites3 , capPerdue3 = heur_naive_trie_selon_poids(listeObj, capBoites)
    boites4 , capPerdue4 = heur_naive_trie_selon_poids_depl_obj(listeObj, capBoites)
    boites5 , capPerdue5 = heur_naive_trie_selon_poids_depl_obj_bis(listeObj, capBoites)
    boites6 , capPerdue6 = heur_naive_trie_selon_poids_depl_obj_ter(listeObj, capBoites)
    boites7 , capPerdue7 = repeter_heur_alea(listeObj, capBoites)
    boites8 , capPerdue8 = heur_naive_trie_selon_poids_depl_obj_quad(listeObj,capBoites)
    print("Capacité perdue heur_naive = " + str(capPerdue1))
    print("Capacité perdue heur_naive_bis = " + str(capPerdue2))
    print("Capacité perdue heur_naive_trie_selon_poids = " + str(capPerdue3))
    print("Capacité perdue heur_naive_trie_selon_poids_depl_obj = " + str(capPerdue4))
    print("Capacité perdue heur_naive_trie_selon_poids_depl_obj_bis = " + str(capPerdue5))
    print("Capacité perdue heur_naive_trie_selon_poids_depl_obj_ter = " + str(capPerdue6))
    print("Capacité perdue heur_alea = " + str(capPerdue7))
    print("Capacité perdue heur_naive_trie_selon_poids_depl_obj_quad = " + str(capPerdue8))
    for boite in boites8:
        print(boite)
