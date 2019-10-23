from heuristiques import *
from classes import *

if __name__ == '__main__':
    
    capBoites , listeObj = chargerBench("../instances/bench_2_0")
    boites1 , capPerdue1 = heur_naive(listeObj, capBoites)
    print("Capacité perdue = " + str(capPerdue1))
    for boite in boites1:
        print(boite)

    with open("resultats.csv" , "w+") as results:
        results.write(",heur_naive,heur_naive_bis,heur_naive_triee_selon_poids\n")
        capBoites , listeObj = chargerBench("../instances/test0")
        boites1 , capPerdue1 = heur_naive(listeObj, capBoites)
        boites2 , capPerdue2 = heur_naive_bis(listeObj, capBoites)
        boites3 , capPerdue3 = heur_naive_trie_selon_poids(listeObj, capBoites)
        boites4 , capPerdue4 = heur_naive_trie_selon_poids_depl_obj(listeObj, capBoites , 0.1)
        newLine = "test0," + str(capPerdue1) + \
                    "," + str(capPerdue2) + "," + str(capPerdue3) + "," + str(capPerdue4) + "\n"
        results.write(newLine)
        
        for i in range(2,21):
            for j in range(0,5):
                nomBench = "../instances/bench_" + str(i) + "_" + str(j)
                capBoites , listeObj = chargerBench(nomBench)
                boites1 , capPerdue1 = heur_naive(listeObj, capBoites)
                boites2 , capPerdue2 = heur_naive_bis(listeObj, capBoites)
                boites3 , capPerdue3 = heur_naive_trie_selon_poids(listeObj, capBoites)
                boites4 , capPerdue4 = heur_naive_trie_selon_poids_depl_obj(listeObj, capBoites , 0.1)
                newLine = 'bench_' + str(i) + "_" + str(j) + "," + str(capPerdue1) + \
                    "," + str(capPerdue2) + "," + str(capPerdue3) + "," + str(capPerdue4) + "\n"
                results.write(newLine)
