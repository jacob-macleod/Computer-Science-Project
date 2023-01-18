function generatePassword() {
    // Generate a random password
    var allowedCharacters = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!£$%^&*()_-+={}[]:@~;'#<>?/.,|".split('');
    var password = "";
    
    for (i=0;i<10;i++){
        indexLocation = Math.round(Math.random() * (allowedCharacters.length-1))
        password = password + allowedCharacters[indexLocation]
    }
    return password
}

