import random
import math
from datetime import datetime, timedelta
from encryption import *

# Generates placeholder data
def generatePlaceholderData(numberOfValues) :
    dataItems = []

    # Generate data according to the following function. Works in Geogebra. Looks a little complicated, but it generates data that trends slightly up or down over a period
    # f(x)=RandomBetween(1,5) sin(RandomBetween(1,3) x)+((RandomBetween(-5,5))/(10)) x
    for i in range(0, numberOfValues):
        x = i/10
        itemToAppend= str(int(random.randint(1,5) * (random.randint(1,5)*x)) + (x*((random.randint(-5,5))/10)))
        dataItems.append(itemToAppend)
    

    return dataItems


# Generate time labels to go along with the placeholder data
# Time is stored in the following collums
# Date (ie, day/month/year, 12/07/2022)
# Time (ie, hour:minute, 14:54)
# For each label, we will combine date and time, to give data in the format: date,time
# If I was actually making the dataloggers, I could decide how often to generate the data. For the purposes of this project, generating new data every hour seems like a good option, since
# The graphs generated by the function will have a good amount of datapoints while still being realistic. This function is designed to generated data for multiple days
def generatePlaceholderLabels(numberOfValues) :
    labels = []
    numberOfDays = math.floor(numberOfValues/24)
    # The number of hours over numberOfDays. For example, if numberOfValues = 44, number of days = round down(44/24) = round down(1.833) = 1 day
    # number of hours = the number of hours in teh remainder, .8333 = .8333 * 24 = 20 hours
    # So if numberOfValues = 44, this denotes 1 day (24 hours) + 20 hours 
    numberOfHours = int(((numberOfValues/24) - (numberOfDays)) * 24)

    #print ((datetime.today() - timedelta(days=7)).strftime("%d/%m/%Y"))

    # For numberOfdays, generate the correct placeholder labels
    for i in range(0, numberOfDays) :
        # Find the date of (number of days - i) days ago
        # For example, if numberOfDays = 2, and today is the 19th, it will ouput the date of the 17th and the 18th
        # Outputs in dd/mm/yyyy format
        date = (datetime.today() - timedelta(numberOfDays - i)).strftime("%d/%m/%Y")
        
        for hour in range(0, 24) :
            # For each hour generate the time
            # Add a the ":00" suffix to the hour. If the hour <10, add the "0" prefix. So if hour=6, time = "06:00"
            if hour < 10:
                time = "0" + str(hour) + ":00"
            else :
                time = str(hour) + ":00"

            # Append the time and data to the labels array
            if date != "" :
                labels.append(date + "*" + time)

    # Now, generate the values for numberOfHours
    currentDate = datetime.today().strftime("%d/%m/%Y")
    for hour in range(0, numberOfHours) :
        # Add a the ":00" suffix to the hour. If the hour <10, add the "0" prefix. So if hour=6, time = "06:00"
        if hour < 10:
            time = "0" + str(hour) + ":00"
        else :
            time = str(hour) + ":00"

        labels.append(currentDate + "*" + time)

    
    return labels



# Save placeholder data to the relevant files
# This will generate data for a single datalogger, and multiple dataloggers can be added
# This will need to be done everytime a user signs up
def savePlaceholderData (numberOfItems, farmID, dataloggerName, id) :
    lightLevels = generatePlaceholderData(numberOfItems)
    humidity = generatePlaceholderData(numberOfItems)
    phLevel = generatePlaceholderData(numberOfItems)
    soilMoisture = generatePlaceholderData(numberOfItems)
    temperature = generatePlaceholderData(numberOfItems)

    # All data will have the same labels
    labels = generatePlaceholderLabels(numberOfItems)

    # Save data to data table
    with open("database/dataTable.csv", 'a') as file:
        for i in range(0, numberOfItems):
            lineToAppend = encrypt(id) + "," + encrypt(labels[i].split("*")[0]) + "," + encrypt(labels[i].split("*")[1]) + "," + encrypt(lightLevels[i]) + "," + encrypt(humidity[i]) + "," + encrypt(phLevel[i]) + "," + encrypt(soilMoisture[i]) + "," + encrypt(temperature[i]) + "\n"
            file.write(lineToAppend)

    # Save data to datalogger table
    with open("database/dataloggerTable.csv", 'a') as file:
        file.write(encrypt(id) + "," + encrypt(farmID) + "," + encrypt(dataloggerName) + "\n")