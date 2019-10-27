from heuristiques import *
from classes import *

if __name__ == '__main__':

    with open("resultats.csv" , "w+") as results:
        results.write(",heur_naive,heur_naive_bis,heur_naive_triee_selon_poids,heur_naive_triee_selon_poids_depl_obj,heur_naive_triee_selon_poids_depl_obj_bis\n")
        capBoites , listeObj = chargerBench("../instances/test0")
        boites1 , capPerdue1 = heur_naive(listeObj, capBoites)
        boites2 , capPerdue2 = heur_naive_bis(listeObj, capBoites)
        boites3 , capPerdue3 = heur_naive_trie_selon_poids(listeObj, capBoites)
        boites4 , capPerdue4 = heur_naive_trie_selon_poids_depl_obj(listeObj, capBoites)
        boites5 , capPerdue5 = heur_naive_trie_selon_poids_depl_obj_bis(listeObj, capBoites)

        newLine = "test0," + str(capPerdue1) + \
                    "," + str(capPerdue2) + "," + str(capPerdue3) + "," + str(capPerdue4) + "," + str(capPerdue5) +"\n"
        results.write(newLine)
        
        for i in range(2,21):
            for j in range(0,5):
                nomBench = "../instances/bench_" + str(i) + "_" + str(j)
                capBoites , listeObj = chargerBench(nomBench)
                boites1 , capPerdue1 = heur_naive(listeObj, capBoites)
                boites2 , capPerdue2 = heur_naive_bis(listeObj, capBoites)
                boites3 , capPerdue3 = heur_naive_trie_selon_poids(listeObj, capBoites)
                boites4 , capPerdue4 = heur_naive_trie_selon_poids_depl_obj(listeObj, capBoites , 0.1)
                boites5 , capPerdue5 = heur_naive_trie_selon_poids_depl_obj_bis(listeObj, capBoites , 0.1)
                newLine = 'bench_' + str(i) + "_" + str(j) + "," + str(capPerdue1) + \
                    "," + str(capPerdue2) + "," + str(capPerdue3) + "," + str(capPerdue4) + "," + str(capPerdue5) +"\n"
                results.write(newLine)
                
    with open("resultats2.csv" , "w+") as results:
        results.write(",heur_naive,heur_naive_bis,heur_naive_triee_selon_poids,heur_naive_triee_selon_poids_depl_obj,heur_naive_triee_selon_poids_depl_obj_bis\n")
        capBoites , listeObj = chargerBench("../instances/test0")
        boites1 , capPerdue1 = heur_naive(listeObj, capBoites)
        boites2 , capPerdue2 = heur_naive_bis(listeObj, capBoites)
        boites3 , capPerdue3 = heur_naive_trie_selon_poids(listeObj, capBoites)
        boites4 , capPerdue4 = heur_naive_trie_selon_poids_depl_obj(listeObj, capBoites)
        boites5 , capPerdue5 = heur_naive_trie_selon_poids_depl_obj_bis(listeObj, capBoites)

        newLine = "test0," + str(capPerdue1) + \
                    "," + str(capPerdue2) + "," + str(capPerdue3) + "," + str(capPerdue4) + "," + str(capPerdue5) +"\n"
        results.write(newLine)
        
        for i in range(2,21):
            for j in range(0,20):
                nomBench = "../instances2/bench_" + str(i) + "_" + str(j)
                capBoites , listeObj = chargerBench(nomBench)
                boites1 , capPerdue1 = heur_naive(listeObj, capBoites)
                boites2 , capPerdue2 = heur_naive_bis(listeObj, capBoites)
                boites3 , capPerdue3 = heur_naive_trie_selon_poids(listeObj, capBoites)
                boites4 , capPerdue4 = heur_naive_trie_selon_poids_depl_obj(listeObj, capBoites , 0.1)
                boites5 , capPerdue5 = heur_naive_trie_selon_poids_depl_obj_bis(listeObj, capBoites , 0.1)
                newLine = 'bench_' + str(i) + "_" + str(j) + "," + str(capPerdue1) + \
                    "," + str(capPerdue2) + "," + str(capPerdue3) + "," + str(capPerdue4) + "," + str(capPerdue5) +"\n"
                results.write(newLine)
                

    print("Résultats enregistrés dans le fichier resultats.csv. Ouvrez ce fichier avec un tableur pour exploiter les résultats obtenus.")