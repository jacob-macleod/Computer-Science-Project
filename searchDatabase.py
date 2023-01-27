# A file of functions to search the database
from datetime import datetime, timedelta
from encryption import *


# Search dataTable.csv to find the data for the specifc day
# Append each line that contains the data into an array
def loadDataForSpecificDay(day, dataloggerID):
    data = []

    # Open the file
    with open("database/dataTable.csv", 'r') as file:
        # for each line
        for line in file:
            # If the dataloggerID is correct
            if decrypt(line.split(",")[0]) == dataloggerID:
                # If the date is correct
                if decrypt(line.split(",")[1]) == day:
                    data.append(decrypt(line.split(",")[2]) + "," + decrypt(line.split(",")[3]) + "," + decrypt(line.split(",")[4]) + "," + decrypt(line.split(",")[5]) + "," + decrypt(line.split(",")[6]) + "," + decrypt(line.split(",")[7]))
    return data

# Turn the data generated by the above code into a string in the format:
# readingType1*value1,value2,value3*readingType2, etc
def turnDataIntoStringFormat(data) :
    lightLevels = ""
    humidity = ""
    phLevel = ""
    soilMoisture = ""
    temperature = ""

    for i in range(0, len(data)) :
        lightLevels = lightLevels + data[i].split(",")[1] + ","
        humidity = humidity + data[i].split(",")[2] + ","
        phLevel = phLevel + data[i].split(",")[3] + ","
        soilMoisture = soilMoisture + data[i].split(",")[4] + ","
        temperature = temperature + data[i].split(",")[5] +","

    return "Light Levels*" + lightLevels + "*Humidity*" + humidity + "*PH Levels*" + phLevel + "*Soil Moisture*" + soilMoisture + "*Temperature*" + temperature
    


# Load the data for the current day
# If no data found, go back a day and repeat again. Repeat until data is found
def loadDataForCurrentDay(farmID) :
    currentDate = datetime.today().strftime("%d/%m/%Y")
    dataloggerID = ""
    data = []
    dataStr = ""

    # Find the first data monitor belonging to the farmID
    with open("database/dataloggerTable.csv", 'r') as file:
        # For each line in the file, if the farmID of the datalogger == farmID, if the dataloggerID has not been set, dataloggerID == dataloggerID associated with farmID
        for line in file:
            if decrypt(line.split(",")[1]) == farmID:
                if dataloggerID == "":
                    dataloggerID = decrypt(line.split(",")[0])

    # Try to load the data for the current day
    # If no data found, go back a day and try this again. Repeat for 100 times
    # If no data is saved in the csv files or the dataloggerID is wrong this will go on for ever, hence why we cap it out at 100 tries
    # If actually deployed, even 100 tries could be too much. I have chosen 100 tries because since I am not actually making the dataloggers, so placeholder data could be generated then
    # No new generated generated for ages. But if I was making the dataloggers, new data should be generated each day so i could be reduced dramatically
    i = 0
    while i < 100:
        # Get the day to look at - at first i = 0 so the day is today, then it goes back a day at a time
        day = (datetime.today() - timedelta(i)).strftime("%d/%m/%Y")

        if loadDataForSpecificDay(day, dataloggerID) == [] :
            i = i + 1
        else:
            data = loadDataForSpecificDay(day, dataloggerID)
            i = 101
        
    if data != [] :
        dataStr = turnDataIntoStringFormat(data)
        dataStr = dataStr + "*" + day
    
    return dataStr

# Get the data for a specifc day, format it, and return it
def loadAndFormatDataForSpecificDay (day, dataloggerID):
    dataStr = ""
    data = loadDataForSpecificDay(day, dataloggerID)
    if data != [] :
        dataStr = turnDataIntoStringFormat(data)
        dataStr = dataStr + "*" + day
    return dataStr

# Finds all the dataloggers owned by the farm ID
def findDataloggersOwnedByFarmID(farmID) :
    dataloggers = ""
    with open("database/dataloggerTable.csv", 'r') as file:
        # For each line in the file, if the farmID of the datalogger == farmID, then save the datalogger name to the array
        for line in file:
            if decrypt(line.split(",")[1]) == farmID:
                dataloggers = dataloggers + (decrypt(line.split(",")[2])) + ","
    
    return dataloggers


# Get the data for a specifc data logger for a specific category over a specific time period
def getDataForTimePeriod (dataloggerID, category, startDate, endDate) :
    # Convert the start and end dates to date time format
    startDate = datetime.strptime(startDate, "%d/%m/%Y")
    endDate = datetime.strptime(endDate, "%d/%m/%Y")

    data = []
    individualdataPoints = ""

    # Turn the start and end dates into a list of dates in between, inclusive
    dates = [startDate + timedelta(days=x) for x in range(0, ((endDate + timedelta(1))-startDate).days)]

    # For each date found
    for day in dates:
        # Get the list of data values as an array
        dailyDataValues = loadDataForSpecificDay(day.strftime("%d/%m/%Y"), dataloggerID)
        # Append each item in this array to the data array
        for i in range(0, len(dailyDataValues)):
            data.append(dailyDataValues[i])

    if category == "lightLevels" :
        collumn = 1
    elif category == "humidiTy" :
        collumn = 2
    elif category == "temperature":
        collumn = 3
    elif category == "phLevel" :
        collumn = 4
    else:
        collumn = 5

    for i in range(0, len(data)) :
        individualdataPoints = individualdataPoints + data[i].split(",")[collumn] + ","

    return individualdataPoints

def generateLabels(startDate, endDate, dataloggerID) :
    # Convert the start and end dates to date time format
    startDate = datetime.strptime(startDate, "%d/%m/%Y")
    endDate = datetime.strptime(endDate, "%d/%m/%Y")

    labels = []
    listOfDays = ""

    # Turn the start and end dates into a list of dates in between, inclusive
    dates = [startDate + timedelta(days=x) for x in range(0, ((endDate + timedelta(1))-startDate).days)]

    # For each date found
    with open("database/dataTable.csv", 'r') as file:
        for line in file:
            for day in dates:
                # If the day == the current day
                if decrypt(line.split(",")[1]) == day.strftime("%d/%m/%Y"):
                    # If the data for this day and time is owned by the correct datalogger
                    if decrypt(line.split(",")[0]) == dataloggerID :
                        print (decrypt(line.split(",")[1]))
                        day = decrypt(line.split(",")[1])
                        day = day.split("/")[0] + "/" + day.split("/")[1]
                        listOfDays = listOfDays + day + " " + decrypt(line.split(",")[2]) + ","
    return listOfDays

# generates labels for today
# If no data stored for today, generate labels for the last avaliable day
def generateLabelsForToday(farmID):
    # Set initial vlaues
    today = str(datetime.today().strftime("%d/%m/%Y"))
    labels = []
    dataloggerID = ""

    # Find the first data monitor belonging to the farmID
    with open("database/dataloggerTable.csv", 'r') as file:
        for line in file:
            if decrypt(line.split(",")[1]) == farmID:
                if dataloggerID == "":
                    dataloggerID = decrypt(line.split(",")[0])

    # Try to load the data for the current day
    # If data is found, generate the labels for that day
    # If no data found, go back a day and try this again. Repeat for 100 times
    # If no data is saved in the csv files or the dataloggerID is wrong this will go on for ever, hence why we cap it out at 100 tries
    # If actually deployed, even 100 tries could be too much. I have chosen 100 tries because since I am not actually making the dataloggers, so placeholder data could be generated then
    # No new generated generated for ages. But if I was making the dataloggers, new data should be generated each day so i could be reduced dramatically
    i = 0
    while i < 100:
        # Get the day to look at - at first i = 0 so the day is today, then it goes back a day at a time
        day = (datetime.today() - timedelta(i)).strftime("%d/%m/%Y")

        if loadDataForSpecificDay(day, dataloggerID) == [] :
            i = i + 1
        else:
            labels = generateLabels(day, day, dataloggerID)
            i = 101  
    return labels