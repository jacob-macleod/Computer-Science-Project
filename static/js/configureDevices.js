// Set up the functionality for the hamburger menu
hamburgerMenu();
// Set up the menu bar of the page
setUpMenuBar(isAdmin);
// If the user is an admin, show pages that are restricted by default
showRestrictedPages(isAdmin);

// Add an element to the table for each of the dataloggers
for (i=0;i<dataloggers.length;i++) {
    if (dataloggers[i] != "") {
        // Create the container to hold the datalogger name and remove button
        container = document.createElement("d");
        container.id = "tableItem";

        // Create the paragraph which holds the datalogger name
        deviceName = document.createElement("p");
        deviceName.innerHTML = dataloggers[i];
        deviceName.id = "itemName";

        // Create the button used to remove the datalogger
        button = document.createElement("button");
        button.innerHTML = "Remove";
        button.setAttribute("onclick", "removeDatalogger()");
        button.setAttribute("name", dataloggers[i]);
        button.id = "outlinedButton";

        // Append deviceName and button to the container
        container.appendChild(deviceName);
        container.appendChild(button);

        // Append the container to the table
        document.getElementById("table").appendChild(container);
    }
}

function removeDatalogger() {
    deviceName = event.target.name;
    if (confirm("Are you sure you want to remove the '" + deviceName + "' datalogger?")) { 
        window.open("/remove-device?deviceName=" + deviceName, "_self");
    }
}