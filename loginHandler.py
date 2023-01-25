# Handles functions related to login
import random
from encryption import *
from generatePlaceholderData import savePlaceholderData

# Generate the ID, which is one bigger than the previous ID
def generateID(fileToRead) :
    highestID = 0

    # For every line in the file, if the ID is bigger than the highest ID, set the highestID to the ID found
    with open(fileToRead, 'r') as file:
        if file == "" :
            return 1
        else:
            for line in file:
                # The first collum will be the ID
                if int(decrypt(line.split(",")[0])) > highestID:
                    highestID = int(decrypt(line.split(",")[0]))

    # The new user ID is 1 bigger than the highest ID used
    return highestID + 1

# Search a file for a username. If found, look for the password belonging to the user. If found, return true, otherwise return false
# Basically, check if the user entered credentials are correct
def searchForCredentials(username, fileToSearch, rowToSearch, password) :
    matchFound = False

    with open(fileToSearch, 'r') as file:
        for line in file:
            # If the username is correct
            if decrypt(line.split(",")[rowToSearch]) == username:
                # If the password is correct
                if decrypt(line.split(",")[5]) == password :
                    matchFound = True


    return matchFound


# Search a file for a value. If the value is found, return another collum in the same row
def findValue(valueToFind, fileToSearch, rowToSearch, columnToReturn) :
    match = ""

    with open(fileToSearch, 'r') as file:
        for line in file:
            if decrypt(line.split(",")[rowToSearch]) == valueToFind:
                match = decrypt(line.split(",")[columnToReturn])

    return match

def createAccount(firstName, lastName, username, password, farmName) :
    # Generate userID
    userID = generateID("database/owners.csv")
    # Generate farmID
    farmID = generateID("database/owners.csv")
    
    savePlaceholderData (153, str(farmID), "Main Datalogger", str(generateID("database/dataloggerTable.csv")))

    # Save the required details to the owners.csv file
    with open("database/owners.csv", "a") as file:
        file.write(encrypt(str(userID)) + "," + encrypt(str(farmID)) + "," + encrypt(firstName) + "," + encrypt(lastName) + "," + encrypt(username) + "," + encrypt(password) + "\n")
    # Save the required details to the farmTable.csv
    with open("database/farmTable.csv", "a") as file:
        file.write(encrypt(str(farmID)) + "," + encrypt(farmName) + "\n")

def getFarmName(username) :
    return findValue(findValue(username, "database/owners.csv", 4, 1), "database/farmTable.csv", 0, 1)

def getFarmID(username) :
    return findValue(findValue(username, "database/owners.csv", 4, 1), "database/farmTable.csv", 0, 0)

def getDataloggerID(dataloggerName) :
    return findValue(dataloggerName, "database/dataloggerTable.csv", 2, 0)

# Remove a datalogger
def removeDatalogger(dataloggerName) :
    dataloggerID = getDataloggerID(dataloggerName)
    dataloggerTable = []
    dataTable = []

    # Read the dataloggerTable.csv file and save each row to an array. If dataloggerName is found, don't save that row
    with open("database/dataloggerTable.csv", "r") as file:
        for line in file:
            lineArr = line.split(",")
            if decrypt(lineArr[2]) != dataloggerName:
                dataloggerTable.append(lineArr[0] + "," + lineArr[1] + "," + lineArr[2])

    # Rewrite the dataloggerTable array back to the file
    with open("database/dataloggerTable.csv", "w") as file:
        for i in range(0, len(dataloggerTable)) :
            file.write(dataloggerTable[i])

    # Read the dataTable.csv file and save each row to an array. If dataloggerName is found, don't save that row
    with open("database/dataTable.csv", "r") as file:
        for line in file:
            lineArr = line.split(",")
            if decrypt(lineArr[0]) != dataloggerID:
                dataTable.append(lineArr[0] + "," + lineArr[1] + "," + lineArr[2] + "," + lineArr[3] + "," + lineArr[4] + "," + lineArr[5] + "," + lineArr[6] + "," + lineArr[7])
    

    # Rewrite the dataloggerTable array back to the file
    with open("database/dataTable.csv", "w") as file:
        for i in range(0, len(dataTable)) :
            file.write(dataTable[i])