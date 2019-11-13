from classes import Boite , Objet , chargerBench
from heuristiques import *

"""
    Effectue des tests sur l'ensemble des benchs et exporte les résultats dans un fichier CSV.
"""

if __name__ == '__main__':
    
    debut = clock()
    tempsParBench = 0.01 # Temps max de résolution par bench (en secondes) sauf pour la méthode aléatoire.

    with open("resultats.csv" , "w+") as results: 
        results.write(",heur_naive,heur_naive_bis,heur_naive_triee_selon_poids,heur_naive_triee_selon_poids_depl_obj,heur_naive_triee_selon_poids_depl_obj_bis,heur_naive_triee_selon_poids_depl_obj_ter,heur_alea,heur_naive_triee_selon_poids_depl_obj_quad\n")
        capBoites , listeObj = chargerBench("../instances/test0")
        boites1 , capPerdue1 = heur_naive(listeObj, capBoites)
        boites2 , capPerdue2 = heur_naive_bis(listeObj, capBoites)
        boites3 , capPerdue3 = heur_naive_trie_selon_poids(listeObj, capBoites)
        boites4 , capPerdue4 = heur_naive_trie_selon_poids_depl_obj(listeObj, capBoites)
        boites5 , capPerdue5 = heur_naive_trie_selon_poids_depl_obj_bis(listeObj, capBoites)
        boites6 , capPerdue6 = heur_naive_trie_selon_poids_depl_obj_ter(listeObj, capBoites)
        boites7 , capPerdue7 = repeter_heur_alea2(listeObj, capBoites)
        boites8 , capPerdue8 = heur_naive_trie_selon_poids_depl_obj_quad(listeObj,capBoites)

        newLine = "test0" + "," + str(capPerdue1) + \
                    "," + str(capPerdue2) + "," + str(capPerdue3) + "," + str(capPerdue4) + "," + str(capPerdue5) + "," + str(capPerdue6) + \
                    "," +  str(capPerdue7) +  "," + str(capPerdue8) + "\n"
        results.write(newLine)
        
        for i in range(2,21):
            for j in range(0,5):
                nomBench = "../instances/bench_" + str(i) + "_" + str(j)
                capBoites , listeObj = chargerBench(nomBench)
                boites1 , capPerdue1 = heur_naive(listeObj, capBoites)
                boites2 , capPerdue2 = heur_naive_bis(listeObj, capBoites)
                boites3 , capPerdue3 = heur_naive_trie_selon_poids(listeObj, capBoites)
                boites4 , capPerdue4 = heur_naive_trie_selon_poids_depl_obj(listeObj, capBoites)
                boites5 , capPerdue5 = heur_naive_trie_selon_poids_depl_obj_bis(listeObj, capBoites)
                boites6 , capPerdue6 = heur_naive_trie_selon_poids_depl_obj_ter(listeObj, capBoites)
                boites7 , capPerdue7 = repeter_heur_alea2(listeObj, capBoites)
                boites8 , capPerdue8 = heur_naive_trie_selon_poids_depl_obj_quad(listeObj,capBoites)
                newLine = "bench_"  + str(i) + "_" + str(j) + "," + str(capPerdue1) + \
                    "," + str(capPerdue2) + "," + str(capPerdue3) + "," + str(capPerdue4) + "," + str(capPerdue5) + "," + str(capPerdue6) + \
                    "," +  str(capPerdue7) +  "," + str(capPerdue8) + "\n"
                results.write(newLine)
                print("bench_{}_{} testé.".format(i,j))
        # Calcul de la moyenne de la capacité perdue lorsque le CSV est exporté dans un tableur
        results.write("Moyenne,=MOYENNE(B2:B97),=MOYENNE(C2:C97),=MOYENNE(D2:D97),=MOYENNE(E2:E97),=MOYENNE(F2:F97),=MOYENNE(G2:G97),=MOYENNE(H2:H97),=MOYENNE(I2:I97)")

                
    # with open("resultats2.csv" , "w+") as results:
    #     results.write(",heur_naive,heur_naive_bis,heur_naive_triee_selon_poids,heur_naive_triee_selon_poids_depl_obj,heur_naive_triee_selon_poids_depl_obj_bis,heur_naive_triee_selon_poids_depl_obj_ter,heur_alea\n")
    #     capBoites , listeObj = chargerBench("../instances2/test0")
    #     boites1 , capPerdue1 = heur_naive(listeObj, capBoites)
    #     boites2 , capPerdue2 = heur_naive_bis(listeObj, capBoites)
    #     boites3 , capPerdue3 = heur_naive_trie_selon_poids(listeObj, capBoites)
    #     boites4 , capPerdue4 = heur_naive_trie_selon_poids_depl_obj(listeObj, capBoites)
    #     boites5 , capPerdue5 = heur_naive_trie_selon_poids_depl_obj_bis(listeObj, capBoites)
    #     boites6 , capPerdue6 = heur_naive_trie_selon_poids_depl_obj_ter(listeObj, capBoites)
    #     boites7 , capPerdue7 = repeter_heur_alea(listeObj, capBoites)

    #     newLine = "test0," + str(capPerdue1) + \
    #                 "," + str(capPerdue2) + "," + str(capPerdue3) + "," + str(capPerdue4) + "," + str(capPerdue5) + "," + str(capPerdue6) + \
    #                 "," +  str(capPerdue7) + "\n"
    #     results.write(newLine)
        
    #     for i in range(2,21):
    #         for j in range(0,20):
    #             nomBench = "../instances2/bench_" + str(i) + "_" + str(j)
    #             capBoites , listeObj = chargerBench(nomBench)
    #             boites1 , capPerdue1 = heur_naive(listeObj, capBoites)
    #             boites2 , capPerdue2 = heur_naive_bis(listeObj, capBoites)
    #             boites3 , capPerdue3 = heur_naive_trie_selon_poids(listeObj, capBoites)
    #             boites4 , capPerdue4 = heur_naive_trie_selon_poids_depl_obj(listeObj, capBoites , tempsParBench)
    #             boites5 , capPerdue5 = heur_naive_trie_selon_poids_depl_obj_bis(listeObj, capBoites , tempsParBench)
    #             boites6 , capPerdue6 = heur_naive_trie_selon_poids_depl_obj_ter(listeObj, capBoites , tempsParBench)
    #             boites7 , capPerdue7 = heur_naive_trie_selon_poids_depl_obj_quad(listeObj, capBoites)
    #             newLine = "bench_"  + str(i) + "_" + str(j) + "," + str(capPerdue1) + \
    #                 "," + str(capPerdue2) + "," + str(capPerdue3) + "," + str(capPerdue4) + "," + str(capPerdue5) + "," + str(capPerdue6) + \
    #                 "," +  str(capPerdue7) + "\n"
    #             results.write(newLine)
    #             print("bench_{}_{} testé.".format(i,j))
    #     # Calcul de la moyenne de la capacité perdue lorsque le CSV est exporté dans un tableur
    #     results.write("Moyenne,=MOYENNE(B2:B382),=MOYENNE(C2:C382),=MOYENNE(D2:D382),=MOYENNE(E2:E382),=MOYENNE(F2:F382),=MOYENNE(G2:G382)")
                
    fin = clock()
    print("Résultats enregistrés dans les fichiers resultats.csv et resultats2.csv. Ouvrez ce fichier avec un tableur pour exploiter les résultats obtenus.")
    print("Exécuté en " + str(fin-debut) + " secondes")
    
    