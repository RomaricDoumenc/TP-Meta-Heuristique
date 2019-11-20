from heuristiques import *
from time import perf_counter
from classes import Objet , Boite , chargerBench , genererBenchAleatoire
import os

if __name__ == "__main__":
    nomFichier = input("Chemin absolu du bench que vous souhaitez tester : ")
    temps = int(input("Temps d'exécution (en secondes) : "))
    if (temps > 60):
        temps = 60
    capBoites,listeObj = chargerBench(nomFichier)
    debut = perf_counter()
    boites1 , capPerdue1 = heur_naive(listeObj, capBoites)
    boites2 , capPerdue2 = heur_naive_bis(listeObj, capBoites)
    boites3 , capPerdue3 = heur_naive_trie_selon_poids(listeObj, capBoites)
    boites4 , capPerdue4 = heur_naive_trie_selon_poids_depl_obj(listeObj, capBoites)
    boites5 , capPerdue5 = heur_naive_trie_selon_poids_depl_obj_bis(listeObj, capBoites)
    boites6 , capPerdue6 = heur_naive_trie_selon_poids_depl_obj_ter(listeObj, capBoites)
    boites7 , capPerdue7 = repeter_heur_alea(listeObj, capBoites , tempsLimite=temps/2)
    boites8 , capPerdue8 = heur_naive_trie_selon_poids_depl_obj_quad(listeObj,capBoites)
    boites9 , capPerdue9 = repeter_heur_alea2(listeObj, capBoites, tempsLimite=temps/2)
    fin = perf_counter()

    for boite in boites9:
        print(boite)

    print("Capacité perdue méthode naive (avec étape prendre les objets de poids égal à un type de boite) = " + str(capPerdue1))
    print("Capacité perdue méthode naive = " + str(capPerdue2))
    print("Capacité perdue méthode naive + tri par ordre décroissant de poids = " + str(capPerdue3))
    print("Capacité perdue méthode naive + exploration de voisinage = " + str(capPerdue4))
    print("Capacité perdue méthode naive + exploration de voisinage (avec étape prendre les objets de poids égal à un type de boite) = " + str(capPerdue5))
    print("Capacité perdue méthode naive + exploration de voisinage (variante objets candidats) = " + str(capPerdue6))
    print("Capacité perdue méthode exploration aléatoire = " + str(capPerdue7))
    print("Capacité perdue méthode prendre les objets 2 par 2 = " + str(capPerdue8))
    print("Capacité perdue méthode prendre les objets 2 par 2 + méthode aléatoire = " + str(capPerdue9))

    
    print("Exécuté en {} secondes.".format(fin-debut))
    os.system("pause")
