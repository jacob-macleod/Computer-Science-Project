import random

# Generates placeholder data
def generatePlaceholderData(numberOfValues) :
    #f(x)=RandomBetween(1,5) sin(RandomBetween(1,3) x)+((RandomBetween(-5,5))/(10)) x
    for i in range(0, numberOfValues) :
        x = i/10
        print (random.randint(1,5))

