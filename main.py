from flask import Flask, request, render_template, make_response
from loginHandler import *
from validateTextFields import *
from searchDatabase import *
from urllib.parse import unquote
# Debug credentials: username = j, password = password123

app = Flask('app', static_url_path='/static')


# Load dashboard page
@app.route("/", methods=["GET", "POST"])
def dashboard():
    isAdmin = False
    passwordFeedbackText = ""
    if request.method == "POST":
        # Sign in the user
        # Get the username and password
        username = request.form.get("username")
        password = request.form.get("password")

        # If the username and passwords match the stored records, that means that they pass the checks since they are stored correctly. Therefore, in the 
        # Sign in stage, no validation or verification checks need to be undertaken

        # If the username and passwords match the stored records:
        loginStatus = searchForCredentials(username, 4, password) 
        if loginStatus != "FAIL":
            # Log the user in
            # Store username as a cookie and load the dashboard page
            isAdmin = loginStatus

            # If the user is an admin, ownerUsername = username
            # if the user is not an admin, ownerUsername = the username of the owner of the user currently logging in
            ownerUsername = findOwnerUsername(isAdmin, username)

            dashboard = make_response(render_template("dashboard.html", isAdmin=isAdmin, firstName=findValue(username, "database/owners.csv", 4, 2), farmName=getFarmName(username), data=loadDataForCurrentDay(getFarmID(ownerUsername)), dataloggers=findDataloggersOwnedByFarmID(getFarmID(ownerUsername)),  labels=generateLabelsForToday(getFarmID(ownerUsername))))
            dashboard.set_cookie('username', username)
            passwordFeedbackText = ""
            return dashboard
        else :
            passwordFeedbackText = "Sorry, your username or password are wrong"
            
    # If user is logged in
    if request.cookies.get("username") != None:
        # If the user is the admin
        if checkIfValueIsUsed(request.cookies.get("username"), "database/owners.csv", 4) == "FAIL":
            isAdmin = True
        # Load dashboard page
        return render_template("dashboard.html", isAdmin=isAdmin, firstName=findValue(request.cookies.get("username"), "database/owners.csv", 4, 2), farmName=getFarmName(request.cookies.get("username")), data=loadDataForCurrentDay(getFarmID(request.cookies.get("username"))), dataloggers = findDataloggersOwnedByFarmID(getFarmID(request.cookies.get("username"))), labels=generateLabelsForToday(getFarmID(request.cookies.get("username"))))
    else:
        # If user is not logged in then load sign in page
        return render_template("signIn.html", passwordFeedbackText=passwordFeedbackText)

@app.route("/advanced-settings")
def advancedSettings () :
    # if the user has logged in before
    if (request.cookies.get("username") != None) :
        # Load the dashboard page
        isAdmin = False
        # See if the user is admin
        if checkIfValueIsUsed(request.cookies.get("username"), "database/owners.csv", 4) == "FAIL":
            isAdmin = True


        data = ""
        labels = ""
        
        # If arguments have been supplied
        if request.args.get("datalogger") != None:
            # Save the results of the arguments
            dataloggerName = request.args.get("datalogger")
            category = request.args.get("category")
            startDate = request.args.get("start")
            endDate = request.args.get("end")
            dataloggerID = getDataloggerID(dataloggerName)

            labels = generateLabels(startDate, endDate, dataloggerID)

            data = getDataForTimePeriod (dataloggerID, category, startDate, endDate)
            
        return render_template("advancedSettings.html", farmName=getFarmName(request.cookies.get("username")), isAdmin=isAdmin, dataloggers = findDataloggersOwnedByFarmID(getFarmID(request.cookies.get("username"))), data=data, labels=labels)
    else :
        # If the user is not logged in load the sign in page
        return render_template("signIn.html")

@app.route("/getDay")
def getDay () :
    # if the user has logged in before
    if (request.cookies.get("username") != None) :
        # Load the dashboard page
        isAdmin = False
        if checkIfValueIsUsed(request.cookies.get("username"), "database/owners.csv", 4) == "FAIL":
            isAdmin = True

        # Find the data for the day selected
        day = request.args.get("day")
        dataloggerName = request.args.get("datalogger")
        dataloggerID = getDataloggerID(dataloggerName)
        data = loadAndFormatDataForSpecificDay(day, dataloggerID)

        labels = generateLabels(day, day, dataloggerID)

        return render_template("dashboard.html", isAdmin=isAdmin, firstName=findValue(request.cookies.get("username"), "database/owners.csv", 4, 2), farmName=getFarmName(request.cookies.get("username")), data=data, dataloggers = findDataloggersOwnedByFarmID(getFarmID(request.cookies.get("username"))), labels=labels)
    else :
        # If the user is not logged in load the sign in page
        return render_template("signIn.html")

# When the sign Up page is loaded
@app.route("/signUp", methods=["GET", "POST"])
def signUp() :
    passwordFeedbackText = ""
    usernameFeedbackText = ""
    firstNameFeedbackText = ""
    lastNameFeedbackText = ""
    farmNameFeedbackText = ""

    # If the user signs up as an admin, this is changed to true
    isAdmin = False
    

    if request.method == "POST" :
        firstName = request.form.get("firstName")
        lastName = request.form.get("lastName")
        username = request.form.get("username")
        password = request.form.get("password")
        passwordConfirmation = request.form.get("passwordConfirmation")
        farmName = request.form.get("farmName")
        
        # Do validation checks
        usernameFeedbackText = applyChecksToUsername(username, "qwertyuiopasdfghjklzxcvbnm-_,.QWERTYUIOPASDFGHJKLZXCVBNM")
        firstNameFeedbackText = applyChecksToName(firstName, "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")
        lastNameFeedbackText = applyChecksToName(lastName, "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM-")
        passwordFeedbackText = applyChecksToPassword(password, passwordConfirmation)
        farmNameFeedbackText = applyChecksToFarmName(farmName, "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm –‘")
        
        # If successful, log user in and create account
        if usernameFeedbackText + firstNameFeedbackText + lastNameFeedbackText + passwordFeedbackText + farmNameFeedbackText == "" :
            # Create the user account
            createAccount(firstName, lastName, username, password, farmName)
            # Return the dashboard page
            # Store username as a cookie and load the dashboard page
            isAdmin = True
            dashboard = make_response(render_template("dashboard.html", isAdmin=isAdmin, firstName=findValue(username, "database/owners.csv", 4, 2), farmName=getFarmName(username), data=loadDataForCurrentDay(getFarmID(username)), dataloggers = findDataloggersOwnedByFarmID(getFarmID(username)), labels=generateLabelsForToday(getFarmID(username))))
            dashboard.set_cookie('username', username)
            passwordFeedbackText = ""
            return dashboard
        
        # If not, the page is reloaded with feedback
    # Return the sign up page
    return render_template("signUp.html", firstNameFeedbackText=firstNameFeedbackText, lastNameFeedbackText=lastNameFeedbackText, passwordFeedbackText=passwordFeedbackText, usernameFeedbackText=usernameFeedbackText, farmNameFeedbackText=farmNameFeedbackText)


# When the configure devices page is loaded
@app.route("/configure-devices")
def configureDevices() :
     # If the user has logged in before
    if (request.cookies.get("username") != None) :
        isAdmin = False

        # If the user is an admin
        if checkIfValueIsUsed(request.cookies.get("username"), "database/owners.csv", 4) == "FAIL":
            isAdmin = True
            return render_template("configureDevices.html", isAdmin=isAdmin, dataloggers=findDataloggersOwnedByFarmID(getFarmID(request.cookies.get("username"))), farmName=getFarmName(request.cookies.get("username")))
        else :
            return render_template("permissionError.html")
    else :
        return render_template("signIn.html")


# When the add-devices page is loaded
@app.route("/add-device", methods=["POST", "GET"])
def addDevices() :
    feedbackText = ""
     # If the user has logged in before
    if (request.cookies.get("username") != None) :
        username = request.cookies.get("username")
        isAdmin = False

        # If the user is an admin
        if checkIfValueIsUsed(username, "database/owners.csv", 4) == "FAIL":
            isAdmin = True

            # Find the name of the datalogger that the user has chosen
            dataloggerName = request.args.get("deviceName")
            if dataloggerName != None:
                # Apply the neccesary checks
                feedbackText = applyChecksToDataloggerName(dataloggerName)
                
                # If there are no errors:
                if feedbackText == "" :
                    # Save all required data for the datalogger
                    savePlaceholderData (153, str(getFarmID(username)), dataloggerName, str(generateID("database/dataloggerTable.csv")))

                    # Return the configure devices page
                    return render_template("configureDevices.html", isAdmin=isAdmin, dataloggers=findDataloggersOwnedByFarmID(getFarmID(request.cookies.get("username"))), farmName=getFarmName(request.cookies.get("username")))

            return render_template("addDevice.html", isAdmin=isAdmin, dataloggers=findDataloggersOwnedByFarmID(getFarmID(username)), farmName=getFarmName(request.cookies.get("username")), feedbackText=feedbackText)
        else :
            return render_template("permissionError.html")
    else :
        return render_template("signIn.html")

# When the user goes to the remove-device page
@app.route("/remove-device", methods=["POST", "GET"])
def removeDevice() :
     # If the user has logged in before
    if (request.cookies.get("username") != None) :
        username = request.cookies.get("username")
        isAdmin = False

        # If the user is an admin
        if checkIfValueIsUsed(username, "database/owners.csv", 4) == "FAIL":
            isAdmin = True

            # Find the name of the datalogger that the user has chosen to delete
            dataloggerName = request.args.get("deviceName")
            if dataloggerName != None:
                # Delete the datalogger
                removeDatalogger(dataloggerName)
                # Return the configure devices page
                return render_template("configureDevices.html", isAdmin=isAdmin, dataloggers=findDataloggersOwnedByFarmID(getFarmID(request.cookies.get("username"))), farmName=getFarmName(request.cookies.get("username")))

            return render_template("addDevice.html", isAdmin=isAdmin, dataloggers=findDataloggersOwnedByFarmID(getFarmID(username)), farmName=getFarmName(request.cookies.get("username")))
        else :
            return render_template("permissionError.html")
    else :
        return render_template("signIn.html")

@app.route("/manage-users")
def manageUsers() :
    # If the user has logged in before
    if (request.cookies.get("username") != None) :
        isAdmin = False

        # If the user is an admin
        if checkIfValueIsUsed(request.cookies.get("username"), "database/owners.csv", 4) == "FAIL":
            isAdmin = True
            return render_template("manageUsers.html", isAdmin=isAdmin, farmName=getFarmName(request.cookies.get("username")), usernames=findDetailsOfWorkersOwnedByOwner(request.cookies.get("username"), 4), firstNames=findDetailsOfWorkersOwnedByOwner(request.cookies.get("username"), 2), lastNames = findDetailsOfWorkersOwnedByOwner(request.cookies.get("username"), 3))
        else :
            return render_template("permissionError.html")
    else :
        return render_template("signIn.html")


@app.route("/add-worker")
def addWorker() :
    # If the user has logged in before
    if (request.cookies.get("username") != None) :
        isAdmin = False

        # If the user is an admin
        if checkIfValueIsUsed(request.cookies.get("username"), "database/owners.csv", 4) == "FAIL":
            isAdmin = True
            return render_template("addWorker.html", isAdmin=isAdmin, farmName=getFarmName(request.cookies.get("username")))
        else :
            return render_template("permissionError.html")
    else :
        return render_template("signIn.html")

@app.route("/make-worker", methods=["POST", "GET"])
def makeWorker() :
    feedbackText = ""
     # If the user has logged in before
    if (request.cookies.get("username") != None) :
        username = request.cookies.get("username")
        isAdmin = False

        # If the user is an admin
        if checkIfValueIsUsed(username, "database/owners.csv", 4) == "FAIL":
            isAdmin = True
            
            # Get details passed through url
            firstName = request.args.get("firstName")
            lastName = request.args.get("lastName")
            workerUsername = request.args.get("username")
            password = request.args.get("password")
            passwordConfirmation = request.args.get("passwordConfirmation")

            # Apply checks and save user
            firstNameFeedbackText = applyChecksToName(firstName, "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")
            lastNameFeedbackText = applyChecksToName(lastName, "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM -")
            usernameFeedbackText = applyChecksToUsername(workerUsername, "qwertyuiopasdfghjklzxcvbnm-_,.")
            passwordFeedbackText = applyChecksToPassword(password, passwordConfirmation)
    
            # If there are no issues with the details entered by the user
            if firstNameFeedbackText + lastNameFeedbackText + usernameFeedbackText + passwordFeedbackText == "":
                # Create the worker
                ownerID = findValue(username, "database/owners.csv", 4, 1)
                createWorker(workerUsername, firstName, lastName, password, ownerID)


                usernames = findDetailsOfWorkersOwnedByOwner(request.cookies.get("username"), 4)
                firstNames = findDetailsOfWorkersOwnedByOwner(request.cookies.get("username"), 2)
                lastNames = findDetailsOfWorkersOwnedByOwner(request.cookies.get("username"), 3)
                # Return the configure devices page
                return render_template("manageUsers.html", isAdmin=isAdmin, farmName=getFarmName(request.cookies.get("username")), firstNameFeedbackText=firstNameFeedbackText, lastNameFeedbackText=lastNameFeedbackText, usernameFeedbackText=usernameFeedbackText, passwordFeedbackText=passwordFeedbackText, usernames=usernames, firstNames=firstNames, lastNames=lastNames)

            else :
                return render_template("addWorker.html", isAdmin=isAdmin, farmName=getFarmName(request.cookies.get("username")), firstNameFeedbackText=firstNameFeedbackText, lastNameFeedbackText=lastNameFeedbackText, usernameFeedbackText=usernameFeedbackText, passwordFeedbackText=passwordFeedbackText)
        else :
            return render_template("permissionError.html")
    else :
        return render_template("signIn.html")

# Remove a worker
@app.route("/remove-worker", methods=["POST", "GET"])
def removeWorker () :
    # If the user has logged in before
    if (request.cookies.get("username") != None) :
        isAdmin = False

        # If the user is an admin
        if checkIfValueIsUsed(request.cookies.get("username"), "database/owners.csv", 4) == "FAIL":
            isAdmin = True

            # Remove the worker
            workerUsername = request.args.get("workerUsername")
            deleteWorker(workerUsername)
            return render_template("manageUsers.html", isAdmin=isAdmin, farmName=getFarmName(request.cookies.get("username")), usernames=findDetailsOfWorkersOwnedByOwner(request.cookies.get("username"), 4), firstNames=findDetailsOfWorkersOwnedByOwner(request.cookies.get("username"), 2), lastNames = findDetailsOfWorkersOwnedByOwner(request.cookies.get("username"), 3))
        else :
            return render_template("permissionError.html")
    else :
        return render_template("signIn.html")

# Return the sign in image when requested
@app.route("/signInImage")
def signInImage():
    return render_template("signInImage.png")

# Return the sign up image when requested
@app.route("/signUpImage")
def signUpImage():
    return render_template("signUpImage.png")

app.run(host='0.0.0.0', port=8080)
