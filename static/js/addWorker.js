function addWorker() {
    firstName = document.getElementsByName("firstName")[0].value;
    lastName = document.getElementsByName("lastName")[0].value;
    username = document.getElementsByName("username")[0].value;
    password = document.getElementById("passwordInputBox").value;
    passwordConfirmation = document.getElementById("passwordConfirmationInputBox").value;
    //console.log (document.getElementsByName("firstName")[0].value);

    pageToLoad = "/make-worker?firstname=" + firstName + "&lastName=" + lastName + "&username=" + username + "&password=" + password + "&passwordConfirmation" + passwordConfirmation;
    alert (pageToLoad);
    //window.open(pageToLoad, "_self");
}