function addWorker() {
    firstName = document.getElementsByName("firstName")[0].value;
    lastName = document.getElementsByName("lastName")[0].value;
    username = document.getElementsByName("username")[1].value;
    password = document.getElementById("passwordInputBox").value;
    passwordConfirmation = document.getElementById("passwordConfirmationInputBox").value;

    pageToLoad = "/make-worker?firstName=" + firstName + "&lastName=" + lastName + "&username=" + username + "&password=" + password + "&passwordConfirmation=" + passwordConfirmation;
    window.open(pageToLoad, "_self");
}

//Select all input boxes
inputBoxes = document.querySelectorAll('input');

// Set the value of the input boxes to equal the equivalent text in the cookie, if the associated feedback text is invisible 
if (getCookie(" workerInputBoxText") == undefined) {
    document.cookie = " workerInputBoxText=,,,,,,";
} else {
    inputBoxText = getCookie(" workerInputBoxText").split(",");
    feedbackTexts = document.getElementsByName("feedbackText");

    for (i=0;i<inputBoxes.length;i++) {
        console.log(i);
        if (feedbackTexts[i].innerHTML == "") {
            inputBoxes[i].value = inputBoxText[i];
        }
     }
}

hamburgerMenu();

// When an input box is clicked
function onInputBoxClick () {
    inputBoxText = "";

    // Append the text in all the input boxes to a string
    for (i=0;i<inputBoxes.length;i++) {
        inputBoxText = inputBoxText + inputBoxes[i].value + ","
    }

    // And save that string as the cookie
     document.cookie = "workerInputBoxText=" + inputBoxText;
}

// For every input box add an event listener
for (i=0;i<inputBoxes.length;i++) {
    inputBoxes[i].addEventListener("keyup", () => {onInputBoxClick()});
}
