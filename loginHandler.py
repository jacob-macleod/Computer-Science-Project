# Handles functions related to login
import random
from encryption import *

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

# Search a file for a specific value. Return true if found, otherwise return false
# For example, you could search the owners.csv file for a specifc user
def searchForValue(valueToFind, fileToSearch, rowToSearch) :
    matchFound = False

    with open(fileToSearch, 'r') as file:
        for line in file:
            if decrypt(line.split(",")[rowToSearch]) == valueToFind:
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
    
    # Save the required details to the owners.csv file
    with open("database/owners.csv", "a") as file:
        file.write(encrypt(str(userID)) + "," + encrypt(str(farmID)) + "," + encrypt(firstName) + "," + encrypt(lastName) + "," + encrypt(username) + "," + encrypt(password) + "\n")
    # Save the required details to the farmTable.csv
    with open("database/farmTable.csv", "a") as file:
        file.write(encrypt(str(farmID)) + "," + encrypt(farmName) + "\n")

def getFarmName(username) :
    return findValue(findValue(username, "database/owners.csv", 4, 1), "database/farmTable.csv", 0, 1)