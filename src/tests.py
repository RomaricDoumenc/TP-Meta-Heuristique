from heuristiques import *
from classes import *

if __name__ == '__main__':
    
    #===========================================================================
    # for i in range(2,21):
    #     for j in range(0,5):
    #         nomBench = "../instances/bench_" + str(i) + "_" + str(j)
    #         with open(nomBench , "r+") as bench:
    #             for k in range(81):
    #                 bench.readline()
    #             bench.seek(bench.tell() - 1)
    #             bench.write('13\t58')
    # 
    #===========================================================================
    
    with open("resultats.csv" , "w+") as results:
        for i in range(2,21):
            for j in range(0,5):
                nomBench = "../instances/bench_" + str(i) + "_" + str(j)
                capBoites , listeObj = chargerBench(nomBench)
                boites1 , capPerdue1 = heur_naive(listeObj, capBoites)
                boites2 , capPerdue2 = heur_naive_bis(listeObj, capBoites)
                boites3 , capPerdue3 = heur_naive_trie_selon_poids(listeObj, capBoites)
                newLine = 'bench_' + str(i) + "_" + str(j) + "," + str(capPerdue1) + \
                    "," + str(capPerdue2) + "," + str(capPerdue3) + ",\n"
                results.write(newLine)


    