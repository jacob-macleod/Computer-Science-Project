// Set up the functionality for the hamburger menu
hamburgerMenu();
// Set up the menu bar of the page
setUpMenuBar(isAdmin);
// If the user is an admin, show pages that are restricted by default
showRestrictedPages(isAdmin);

function addDevice() {
    deviceName = document.getElementById('inputBoxText').value; 
    window.open("/add-device?deviceName=" + deviceName, "_self");
}