from GA import GA
import networkx as nx
import scipy as sp
import matplotlib.pyplot as plt

def readData(filename):
    G = nx.read_gml(filename,label='id')

    net = {}
    net['noNodes'] = G.number_of_nodes()
    net['mat'] = nx.adjacency_matrix(G).todense()
    net['noEdges'] = G.number_of_edges()
    net['degrees'] = [val for (node, val) in G.degree()]
    net['graph'] = G
    return net

def modularity(communities, param):
    noNodes = param['noNodes']
    mat = param['mat']
    degrees = param['degrees']
    noEdges = param['noEdges']
    M = 2 * noEdges
    Q = 0.0
    for i in range(0, noNodes):
        for j in range(0, noNodes):
            if (communities[i] == communities[j]):
                Q += (mat.item(i,j) - degrees[i] * degrees[j] / M)
    return Q * 1 / M

net = readData('myCommunity.gml')
gaParam = {"popSize": 1000, "noGen": 7, "pc": 0.8, "pm": 0.1, "network": net}
problParam = {'function': modularity, 'retea': net}

def afisare(x):
    comunities=[]
    for i in range(0,problParam['retea']['noNodes']+1):
        comunities.append([])
    for i in range(0,net['noNodes']):
        comunities[x[i]].append(i+1)
    j=0
    while j < len(comunities):
        if comunities[j] == []:
            comunities.pop(j)
        else:
            j+=1
    return comunities

def main():
    ga = GA(gaParam, problParam)
    ga.initialisation()
    ga.evaluation()

    stop = False
    g = -1
    while (not stop and g < gaParam['noGen']):
        g += 1
        ga.oneGeneration()

        bestChromo = ga.bestChromosome()
        print('Solutia cea mai buna in generatia ' + str(g) + ' este: ' + str(afisare(bestChromo.repres)) + ' f(x) = ' + str(
            bestChromo.fitness) + ' ' + 'Numar comunitati:' + str(len(afisare(bestChromo.repres))))

main()
