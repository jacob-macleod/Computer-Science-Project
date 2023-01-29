function togglePasswordVisibility () {
    // Get some variables
    var passwordBox = document.getElementsByName("password")[0];
    passwordBoxType = passwordBox.getAttribute("type");
    button = document.getElementsByName("togglePassword")[0];

    // If the password is hidden
    if (passwordBoxType == "password") {
        // Then show the password
        passwordBox.setAttribute("type", "");
        button.innerHTML = "Hide Password"
    } else { // Else if the password is not hidden
        // Then hide the password
        passwordBox.setAttribute("type", "password");
        button.innerHTML = "Show Password"
    }
    event.preventDefault();
}