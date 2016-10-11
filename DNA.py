from random import randint

# A class to describe a pseudo-DNA, i.e. genotype
#   Here, a virtual organism's DNA is an array of character.
#   Functionality:
#      -- convert DNA into a string
#      -- calculate DNA's "fitness"
#      -- mate DNA with another set of DNA
#      -- mutate DNA

def newCharacter ():
    c = randint(63,122)
    if c == 63:
        c = 32;
    if c ==64: 
        c = 46;
    
    return chr(c)

class DNA:
    def __init__( self, num):
#   The genetic sequence
        self.genes = []
        self.fitness = 0.
        for  i in range (0, num):
            self.genes.append(newCharacter());  # Pick from range of chars
#        print self.genes        
        
    def getPhrase ( self):
        return ''.join(self.genes)

#   Fitness function (returns floating point % of "correct" characters)
    
    def calcFitness (self,target):        
        targetList = list(target)        
        score = 0.;
        for i in range (len(target)):
            if (self.genes[i] == targetList[i]):  
                score = score + 1.;
                
        self.fitness = score / float(len(target))
#        print self.fitness

#    Crossover
    def crossover (self, partner):
        child = DNA(len(self.genes))
        midpoint = int(randint(0, len(self.genes))) # Pick a midpoint
    
#    Half from one, half from the other
        for i in range (len(self.genes)) : 
            if (i > midpoint):
                child.genes[i] = self.genes[i]
            else:
              child.genes[i] = partner.genes[i]
        return child
        

#   Based on a mutation probability, picks a new random character
    def mutate( self, mutationRate):
        for i in range (len(self.genes)):
            chanceForMutation = float(randint(0,100))/100.
            if (chanceForMutation < mutationRate):
                self.genes[i] = newCharacter()