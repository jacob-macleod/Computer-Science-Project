/*
    Contains common functions used by multiuple files
*/

// Provides the functionality for the hamburger menu, if it is visible
// When the user clicks the hamburger icon, change the icon and show the hamburger menu. When the user clicks it again, do the opposite
function hamburgerMenu () {
    // Get the icon for the hamburger menu
    icon = document.getElementById("hamburgerIcon");

    // When the icon is clicked
    icon.addEventListener("click", () => {
        // Switch the image that it displays to the image
        // Either "Hamburger.svg" or "close.svg" is shown
        if (icon.getAttribute("src") == "static/img/Hamburger.svg") {
	        icon.setAttribute("src", "static/img/close.svg");
            document.getElementById("menuItems").style.display = "grid";
        } else {
            icon.setAttribute("src", "static/img/Hamburger.svg")
            document.getElementById("menuItems").setAttribute("style", "display:none;")
        }
    });
}

// Delete all cookies
function deleteCookies() {
    // Get all the cookies
    var cookies = document.cookie.split(";");

    // For every cookie, edit it to make it expire
    for (var i = 0; i < cookies.length; i++) {
        var cookie = cookies[i];
        var value = cookie.indexOf("=");
        var name = value > -1 ? cookie.substr(0, value) : cookie;
        // To delete it, make it so it's already expired
        document.cookie = name + "=;expires=Thu, 01 Jan 1970 00:00:00 GMT";
    }
}

// Logout the user
function logout() {
    // Delete all cookies and load the / page. Since there are no cookies the sign in page will load
    deleteCookies();
    window.open("/", "_self");
}

// Get the value of a cookie by it's name
function getCookie(cookieName) {
    singleCookie = decodeURIComponent(document.cookie)
    singleCookie = singleCookie.toString();
    singleCookie = singleCookie.split(";");

    // Look at every cookie
    for (i=0;i<singleCookie.length;i++) {
        // If the cookie's name is right
        if (singleCookie[i].split("=")[0] == cookieName) {
            // Return the cookie's value
            return singleCookie[i].split("=")[1];
        }
    }    
}

/* 
    Set up the menu bar of the page. This includes:
    * Making the admin indicator work
    * Making the admin indicator blue if the user is an admin
    * Setting the username and farm name
*/
function setUpMenuBar (isAdmin) {
    // Set up farm name and username
    document.getElementsByName("username")[0].innerHTML = getCookie("username");

    // Make the admin indicator blue if the user is an owner
    if (isAdmin == "True") {
        document.getElementsByName("adminIndicator")[0].innerHTML = "Owner";
        document.getElementsByName("adminIndicator")[0].style = "display: inline-block; color: #A6CEE3;";
    }
}

// Fill the datalogger select element with values
function fillDataloggerSelectElementWithValues() {
    dataloggersArr = dataloggers.split(",");
    for (i=0;i<dataloggersArr.length;i++) {
            if (dataloggersArr[i] != "") {
            option = document.createElement("option");
            option.value = dataloggersArr[i];
            option.innerHTML = dataloggersArr[i];
            document.getElementById("dataloggerSelector").appendChild(option);
        }
    }
}

function showRestrictedPages (isAdmin) {
    // Some pages are hidden by default. If the user is an admin, show them
    if (isAdmin == "True") {
        // Get all the items to hide
        itemsToHide = document.getElementsByName("restrictedItem");
        for (i=0;i<itemsToHide.length;i++) {
            // Change their visibility to hidden
            itemsToHide[i].style = "display: inline-block; visibility:visible;";
        }
    }
}

// Set up a chart
function drawChart(elementToDrawOn, labels, data, name, color1, color2) {
    // Set up the light level chart
    const ctx = elementToDrawOn;
        
    // Create gradient
    let gradient = ctx.getContext('2d').createLinearGradient(0, 0, 400, 0);
    gradient.addColorStop(0, color1);
    gradient.addColorStop(1, color2);

    // Create chart
    new Chart(ctx, {
    type: 'line',
    data: {
    labels: labels,
    datasets: [{
        label: name,
        data: data,
        fill: false,
        borderColor: gradient,
        tension: 0.05
    }]
    },
    options:  {
        maintainAspectRatio:false
    }
    });
    }