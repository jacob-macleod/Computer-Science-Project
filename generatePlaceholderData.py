import random

# Generates placeholder data
def generatePlaceholderData(numberOfValues) :
    dataItems = []

    # f(x)=RandomBetween(1,5) sin(RandomBetween(1,3) x)+((RandomBetween(-5,5))/(10)) x
    for i in range(0, numberOfValues):
        x = i/10
        itemToAppend= (random.randint(1,5) * (random.randint(1,5)*x)) + (x*((random.randint(-5,5))/10))
        dataItems.append(itemToAppend)
    

    return dataItems



def generatePlaceholderLabels(numberOfValues) :
    labels = []

    for i in range(0, numberOfValues):
        labels.append(i)
    
    return labels

# TODO: Write functions to put the text in the following files:
# Dataloggertable - stores dataloggerID, farmID, dataloggerName
# Data table - stores dataloggerID, date, time, lightlevels, humidity, ph level, soil moisture, temperature