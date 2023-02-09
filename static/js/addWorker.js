function addWorker() {
    firstName = document.getElementsByName("firstName")[0].value;
    lastName = document.getElementsByName("lastName")[0].value;
    username = document.getElementsByName("username")[1].value;
    password = document.getElementById("passwordInputBox").value;
    passwordConfirmation = document.getElementById("passwordConfirmationInputBox").value;

    pageToLoad = "/make-worker?firstName=" + firstName + "&lastName=" + lastName + "&username=" + username + "&password=" + password + "&passwordConfirmation=" + passwordConfirmation;
    window.open(pageToLoad, "_self");
}
