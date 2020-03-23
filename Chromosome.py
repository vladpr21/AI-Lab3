from random import randint
from utils import reprez,generateNewValue


# Binary representation
class Chromosome:
    def __init__(self, problParam=None):
        self.__problParam = problParam
        self.__repres = reprez(problParam['retea'])
        self.__fitness = 0.0

    @property
    def repres(self):
        return self.__repres

    @property
    def fitness(self):
        return self.__fitness

    @repres.setter
    def repres(self, l=[]):
        self.__repres = l

    @fitness.setter
    def fitness(self, fit=0.0):
        self.__fitness = fit

    def crossover(self, c):
        offspring = Chromosome(self.__problParam)
        pos = randint(0, c.__problParam['retea']['noNodes'] - 1)
        val=c.__repres[pos]
        offspring.__repres = [self.__repres[i] if c.__repres[i]!=val else val for i in
                              range(self.__problParam['retea']['noNodes'])]
        return offspring

    def mutation(self):
        pos = randint(0, self.__problParam['retea']['noNodes']-1)
        self.__repres[pos] = self.__repres[generateNewValue(0, self.__problParam['retea']['noNodes']-1)]

    def __str__(self):
        return '\nChromo: ' + str(self.__repres) + ' has fit: ' + str(self.__fitness)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, c):
        return self.__repres == c.__repres and self.__fitness == c.__fitness