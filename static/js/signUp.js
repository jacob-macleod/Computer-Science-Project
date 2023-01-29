//Select all input boxes
inputBoxes = document.querySelectorAll('input');

// Set the value of the input boxes to equal the equivalent text in the cookie, if the associated feedback text is invisible 
if (getCookie("inputBoxText") == undefined) {
    document.cookie = "inputBoxText=,,,,,,";
} else {
    inputBoxText = getCookie("inputBoxText").split(",");
    feedbackTexts = document.getElementsByName("feedbackText");

    for (i=0;i<inputBoxText.length-1;i++) {
        if (feedbackTexts[i].innerHTML == "") {
            inputBoxes[i].value = inputBoxText[i];
        }
     }
}

// When an input box is clicked
function onInputBoxClick () {
    inputBoxText = "";

    // Append the text in all the input boxes to a string
    for (i=0;i<inputBoxes.length;i++) {
        inputBoxText = inputBoxText + inputBoxes[i].value + ","
    }

    // And save that string as the cookie
     document.cookie = "inputBoxText=" + inputBoxText;
}

// For every input box add an event listener
for (i=0;i<inputBoxes.length;i++) {
    inputBoxes[i].addEventListener("keyup", () => {onInputBoxClick()});
}

function togglePasswordVisibility () {
    // Get some variables
    passwordBox = document.getElementsByName("password")[0];
    passwordConfirmationBox = document.getElementsByName("passwordConfirmation")[0];
    passwordBoxType = passwordBox.getAttribute("type");
    button = document.getElementsByName("togglePassword")[0];

    // If the password is hidden
    if (passwordBoxType == "password") {
        // Then show the password
        passwordBox.setAttribute("type", "");
        passwordConfirmationBox.setAttribute("type", "");
        button.innerHTML = "Hide Password"
    } else { // Else if the password is not hidden
        // Then hide the password
        passwordBox.setAttribute("type", "password");
        passwordConfirmationBox.setAttribute("type", "password");
        button.innerHTML = "Show Password"
    }
    event.preventDefault();
}