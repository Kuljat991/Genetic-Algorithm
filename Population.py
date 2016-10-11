from DNA import DNA
from random import randint
from scipy.interpolate import interp1d

#   A class to describe a population of virtual organisms
#   In this case, each organism is just an instance of a DNA object

class Population:
    def __init__(self, p, m, num):
        self.maxFitness = 0.0
        self.population = []    #   Array to hold the current population
        self.matingPool = []    #   ArrayList which we will use for our "mating pool"
        self.generations = 0    #   Number of generations
        self.finished = False   #   Are we finished evolving?
        self.target = p         #   Target phrase
        self.mutationRate = m   #   Mutation rate
        self.perfectScore = 1.
        
        for i in range (num):
            x = DNA(len (self.target))
            self.population.append(x)
            
#        self.calcFitness()
#        self.naturalSelection()
#        mapFitness = interp1d ([0, self.maxFitness],[ 0, 100])
#        for i in range (len(self.population)):
#            fitness = mapFitness(self.population[i].fitness)
#            n = int(fitness)
#            for i in range (n):
#                self.matingPool.append(self.population[i])
#        print len(self.matingPool)
#        self.generate()
#        self.evaluate()
    
    # Fill our fitness array with a value for every member of the population
    def calcFitness (self):
        for i in range (len(self.population)):
            self.population[i].calcFitness(self.target)
#            print self.population[i].fitness
    
    # Generate a mating pool
    def naturalSelection (self):
        self.matingPool = []
        for i in range (len(self.population)): 
            if (self.population[i].fitness > self.maxFitness):
                self.maxFitness = self.population[i].fitness;
#                print self.maxFitness
        mapFitness = interp1d ([0, self.maxFitness],[ 0, 100])
        for i in range (len(self.population)):
            fitness = mapFitness(self.population[i].fitness)
            n = int(fitness)
            for j in range (n):
                self.matingPool.append(self.population[i])
#        print len(self.matingPool)
    
    # Create a new generation
    def generate (self):
    #Refill the population with children from the mating pool
        for i in range (len(self.population)):
            a = int(randint(0, len(self.matingPool)-1))
            b = int(randint(0, len(self.matingPool)-1))
#            print len(self.population)
#            print len(self.matingPool)
            partnerA = self.matingPool[a]
            partnerB = self.matingPool[b]
            child = partnerA.crossover(partnerB)
            child.mutate(self.mutationRate)
            self.population[i] = child
    
        self.generations = self.generations+1;
    
    # Compute the current "most fit" member of the population
    def evaluate (self):
        self.worldrecord = 0.
        index = 0
        for i in range (len(self.population)):
            if (self.population[i].fitness > self.worldrecord):
                index = i
                self.worldrecord = self.population[i].fitness
        
        self.best = self.population[index].getPhrase()
        print self.best
#        print self.population[i].finess
#        print len(self.best)
        
        if (self.worldrecord == self.perfectScore):
            self.finished = True
            print str(self.finished)
        
    def isFinished (self):
        return self.finished
    