# Caeser cipher with a key of 1
# Outputs a list of blocks of two letters where each block corrosponds to a single letter
def encrypt(string):
    number = ""

    allowedCharacters = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM\|1234567890!”£$%^&*()`¬-_=+{}[]:@;’~#<>,.?/  "
    # For every letter in the string, find it's number in allowed characters
    # Then add one to that number
    # Then combine the numbers to one variable
    for letter in string:
        for i in range(0, len(allowedCharacters)):
            if letter == allowedCharacters[i]:
                # Add a 0 in front of i if needed - we need a list of numbers where each value corrospinding to a single letter has a length of 2
                if i < 9:
                    iStr = str(i + 1)
                    iStr = "0" + iStr
                else:
                    iStr = str(i + 1)
                number = number + iStr

    return str(number)


# For every block of 2 in strNumber, subtract 1 from the number and see what letter it corrosponds to from allowedCharacters
def decrypt(strNumber):
    number = strNumber
    string = ""
    allowedCharacters = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM\|1234567890!”£$%^&*()`¬-_=+{}[]:@;’~#<>,.?/  "

    numberArr = []
    #Change number into blocks of two
    for i in range(0, len(number) - 1, 2):
        numberArr.append(number[i] + number[i + 1])

    # Match up these blocks of two to a value
    for value in numberArr:
        for i in range(0, len(allowedCharacters)):
            if (int(value) == i):
                string = string + allowedCharacters[i - 1]

    return string
