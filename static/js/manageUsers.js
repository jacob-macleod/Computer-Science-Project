// Add an element to the table for each of the added workers
for (i=0;i<usernames.length;i++) {
    if (usernames[i] != "") {
        // Create the container to hold the worker details and remove button
        container = document.createElement("d");
        container.id = "tableItem";

        // Create the container to hold the worker's details
        userContainer = document.createElement("d");
        userContainer.setAttribute("style", "display:inline-grid;")

        // Create the paragraph which holds the workers 's names
        workerName = document.createElement("p");
        workerName.innerHTML = firstNames[i] + " " + lastNames[i];
        workerName.id = "itemName";

        // Create the paragraph which hold the worker's usernames
        workerUsername = document.createElement("p");
        workerUsername.innerHTML = usernames[i];
        workerUsername.id = "normalText";
        workerUsername.setAttribute("style", "margin: 0px;")


        // Create the button used to remove the datalogger
        button = document.createElement("button");
        button.innerHTML = "Remove";
        button.setAttribute("onclick", "removeWorker()");
        button.setAttribute("name", usernames[i]);
        button.id = "outlinedButton";

        // Append username and first and last names to userContainer
        userContainer.appendChild(workerName)
        userContainer.appendChild(workerUsername)

        // Append userContainer and button to the container
        container.appendChild(userContainer);
        container.appendChild(button);

        // Append the container to the table
        document.getElementById("table").appendChild(container);
    }
}

hamburgerMenu();

// If no user has been added
if (usernames == "") {
    document.getElementById("table").setAttribute("style", "display:none;");
    document.getElementById("feedbackText").innerHTML = "You haven't added any workers yet"
}

// Clear the workerInputBoxText cookie
document.cookie = "workerInputBoxText=,,,,";

// Remove the worker with the username equal to the name of the button
function removeWorker() {
    workerUsername = event.target.name;
    if (confirm("Are you sure you want to remove the user '" + workerUsername + "'?")) { 
        window.open("/remove-worker?workerUsername=" + workerUsername, "_self");
    }
}
