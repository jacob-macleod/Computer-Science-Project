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


# Search owners.csv for the username and password. If the credentials match a row in the file, return True
# Next, search workertable.csv in the same way, returning False if a match is found
# If no match is found, return "FAIL". If a match is found, isAdmin in main.py can be set to the value indicated by the function
# So, this file can return a boolean or a string. This is only possible in languages like python, but allows for simpler code
def searchForCredentials(username, rowToSearch, password) :
    matchFound = "FAIL"

    with open("database/owners.csv", 'r') as file:
        for line in file:
            # If the username is correct
            if decrypt(line.split(",")[rowToSearch]) == username:
                # If the password is correct
                if decrypt(line.split(",")[5]) == password :
                    matchFound = True
                    
    with open("database/workerTable.csv", 'r') as file:
        for line in file:
            # If the username is correct
            if decrypt(line.split(",")[rowToSearch]) == username:
                # If the password is correct
                if decrypt(line.split(",")[5]) == password :
                    matchFound = False



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

# Create a worker
def createWorker(username, firstName, lastName, password, ownerID) :
    # Make a workerID
    workerID = generateID("database/workerTable.csv")

    # Define the line to append to create the worker
    lineToAppend = encrypt(str(workerID)) + "," + encrypt(str(ownerID)) + "," + encrypt(firstName) + "," + encrypt(lastName) + "," + encrypt(username) + "," + encrypt(password) + "\n"

    # Append lineToAppend to workerTable.csv
    with open("database/workerTable.csv", "a") as file:
        file.write(lineToAppend)

def deleteWorker (username) :
    workerArr = []

    # Copy the data from workerTable to an array
    with open("database/workerTable.csv", "r") as workerTable:
        for line in workerTable:
            # If the line contains data for the worker to be removed, do not copy it
            if line != "" and decrypt(line.split(",")[4]) != username:
                workerArr.append(line)

    # Copy the data from the array to workersTable, overwriting it
    with open("database/workerTable.csv", "w") as workerTable:
        for i in range(0, len(workerArr)) :
            workerTable.write(workerArr[i])
            

# If the user is an admin, return the username given
# If the user is a worker, return the username of the owner of the user
def findOwnerUsername (isAdmin, username) :
    if isAdmin == True:
        ownerUsername = username
        # If the user is not an admin
    elif isAdmin == False :
        # Find the owner ID of the worker
        ownerID = findValue(username, "database/workerTable.csv", 4, 1)
        # Find the username of the owner ID
        ownerUsername = findValue(ownerID, "database/owners.csv", 0, 4)
    return ownerUsername
