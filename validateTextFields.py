# Apply the validationChecks in validationTests.py to different items
from tabnanny import check
from validationTests import *


# Applied the required validation checks to the username input field
def applyChecksToUsername(username, allowedCharacters):
    messageToReturn = ""
    
    if presenceCheck(username) != "PASS":
        messageToReturn = "You need to enter your username"

    if checkIfValueIsUsed(username, "database/owners.csv", 4) != "PASS":
        messageToReturn = "This username is already taken!"

    if checkForAllowedCharacters(username, allowedCharacters) != "PASS":
        messageToReturn = "Sorry, you can only use " + allowedCharacters + " for the username"

    return messageToReturn

# Apply the required checks to the name input field
def applyChecksToName(name, allowedCharacters) :
    messageToReturn = ""
    if presenceCheck(name) != "PASS" :
        messageToReturn = "Sorry, you need to enter text here"
    if checkForAllowedCharacters(name, allowedCharacters) != "PASS":
        messageToReturn = "Sorry, only the following characters are allowed: qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"

    return messageToReturn

# Apply the required checks to the password input field
def applyChecksToPassword(password, passwordConfirmation) :
    messageToReturn = ""

    if lengthCheck(password, 6) != "PASS" :
        messageToReturn = "Sorry, your password should be at least 6 characters long"
    if checkIfStringContainsLettersAndNumbers(password) != "PASS" :
        messageToReturn = "Sorry, your password should contain both letters and numbers"
    if password != passwordConfirmation :
        messageToReturn = "Sorry, your two passwords don’t match"
    if presenceCheck(password) != "PASS" :
        messageToReturn = "Sorry, you need to enter your password"

    return messageToReturn

# Apply the required checks to the farm name input field
def applyChecksToFarmName(farmName, allowedCharacters) :
    messageToReturn = ""

    if presenceCheck(farmName) != "PASS" :
        messageToReturn = "Sorry, you need to enter a name into the box"
    if checkForAllowedCharacters(farmName, allowedCharacters) != "PASS" :
        messageToReturn = "Sorry, the only allowed characters are " + allowedCharacters
    if checkIfValueIsUsed(farmName, "database/farmTable.csv", 1) != "PASS" :
        messageToReturn = "Sorry, that name has already been used"

    return messageToReturn

# Apply the required checks to the datalogger input field
def applyChecksToDataloggerName(dataloggerName) :
    messageToReturn = ""
    if presenceCheck(dataloggerName) != "PASS" :
        messageToReturn = "Sorry, you need to enter the datalogger name"
    if checkForAllowedCharacters(dataloggerName, "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM- _") != "PASS" :
        messageToReturn = "Sorry, only alphabetical characters, spaces, _ and – are allowed"
    if checkIfValueIsUsed(dataloggerName, "database/dataloggerTable.csv", 2) != "PASS":
        messageToReturn = "Sorry, there already is a datalogger with that name"

    return messageToReturn