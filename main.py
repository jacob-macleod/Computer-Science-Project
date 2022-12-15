from flask import Flask, request, render_template, make_response
from loginHandler import *
from validateTextFields import *
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
        if searchForCredentials(username, "database/owners.csv", 4, password) == True:
            # Log the user in
            # Store username as a cookie and load the dashboard page
            isAdmin = True
            dashboard = make_response(render_template("dashboard.html", isAdmin=isAdmin, firstName=findValue(username, "database/owners.csv", 4, 2), farmName=getFarmName(username)))
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
        #print (findValue(request.cookies.get("username"), "database/owners.csv", 4, 1))
        return render_template("dashboard.html", isAdmin=isAdmin, firstName=findValue(request.cookies.get("username"), "database/owners.csv", 4, 2), farmName=getFarmName(request.cookies.get("username")))
    else:
        # If user is not logged in then load sign in page
        return render_template("signIn.html", passwordFeedbackText=passwordFeedbackText)


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
            dashboard = make_response(render_template("dashboard.html", isAdmin=isAdmin, firstName=findValue(username, "database/owners.csv", 4, 2), farmName=getFarmName(username)))
            dashboard.set_cookie('username', username)
            passwordFeedbackText = ""
            return dashboard
        
        # If not, the page is reloaded with feedback
    # Return the sign up page
    return render_template("signUp.html", firstNameFeedbackText=firstNameFeedbackText, lastNameFeedbackText=lastNameFeedbackText, passwordFeedbackText=passwordFeedbackText, usernameFeedbackText=usernameFeedbackText, farmNameFeedbackText=farmNameFeedbackText)

# Return the sign in image when requested
@app.route("/signInImage")
def signInImage():
    return render_template("signInImage.png")

# Return the sign up image when requested
@app.route("/signUpImage")
def signUpImage():
    return render_template("signUpImage.png")

app.run(host='0.0.0.0', port=8080)
