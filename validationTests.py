#Contains Validation Checks
# If passed, all checks return "PASS". If failed, all checks return an error message
from encryption import *

# Presence Check
def presenceCheck (stringToCheck) :
    # Return 0 (fail) if the string is blank, otherwise return 1(pass)
    if stringToCheck == "" :
        return "FAIL"
    else :
        return "PASS"

# Checks a string to see if it is longer than the required length
def lengthCheck(string, length) :
    if len(string) >= length:
        return "PASS"
    else :
        return "FAIL"

# Check if a string contains both letters and numbers
def checkIfStringContainsLettersAndNumbers(string) :
    # Set some initial value
    letters = list("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")
    numbers = list("1234567890")
    containsLetters = False 
    containsNumbers = False 

    # For each letter in the string
    for i in range(0, len(string)) :
        # If it is a number, the string contains a number
        for number in numbers:
            if list(string)[i] == number:
                containsNumbers = True

        # If it is a letter, the string contains a letter
        for letter in letters:
            if list(string)[i] == letter:
                containsLetters = True

    # Return pass or fail
    if containsLetters == True and containsNumbers == True:
        return "PASS"
    else:
        return "FAIL"

# Check if value has already been used
# Searches rows of a specific collum of a specifc file to check if a value has already been used
# For example, you could check if a username has already been used
def checkIfValueIsUsed(value, fileToSearch, collumToSearch) :
    # Set initial value
    matchFound = "PASS"

    # Look at every line in file to search
    with open(fileToSearch, 'r') as file:
        for line in file:
            # Look at the required collum of the file
            if decrypt(line.split(",")[collumToSearch]) == value:
                # If a match is found, change matchFound to an error message
                # If a match is found, pass will be returned
                # If a match is never found, matchFound will never be set to pass, so will remain at an error message, the default value, so an error message will be returned
                matchFound = "FAIL"

    return matchFound

# See if only the allowed characters are included
def checkForAllowedCharacters(string, allowedCharacters) :
    # Set some variables
    checkStatus = "PASS"
    allowedCharactersStr = allowedCharacters
    allowedCharacters = list(allowedCharacters)
    string = list(string)

    # For each letter in string, check if it has a letter in allowed characters. If not, set checkStatus to an error message
    for character in string :
        matchFound = False
        for char in allowedCharacters:
            # Check character to see if it is allowed. If it is, matchFound will be set to True, otherwise it is kept at it's default value of False
            if character == char:
                matchFound = True
        # If false, a character is present which is not in allowed characters
        if matchFound == False:
            checkStatus = "FAIL"

    # Return checkStatus - by default it is equal to "PASS", and will only change if a character in string which is not in allowed characters is found
    return checkStatus