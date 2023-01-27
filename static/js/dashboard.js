// Set up the functionality for the hamburger menu
hamburgerMenu();
// Set up the menu bar of the page
setUpMenuBar(isAdmin);
// If the user is an admin, show pages that are restricted by default
showRestrictedPages(isAdmin);
// Fill the datalogger select element with values
fillDataloggerSelectElementWithValues();

// Find current day
today = new Date();
// Find current year
year = today.getFullYear();
// Find the current month, then add a 0 at the start if teh date is less than 10. So 7 turns to 07
month = parseInt(today.getMonth()) + 1;
if (month < 10) {
    month = "0" + month.toString();
} else {
    month = month.toString();
}

// Do the same as we did for the month for the day
day = parseInt(today.getDate());
if (day < 10) {
    day = "0" + day.toString();
} else {
    day = day + day.toString();
}

date = year + "-" + month + "-" + day;

// Make the date selector show the date for today
document.getElementById("dateSelector").setAttribute("value", date);

function changeDaySelected() {
    day = document.getElementById("dateSelector").value;
    formattedDay = day.split("-")[2] + "/" + day.split("-")[1] + "/" + day.split("-")[0];
    datalogger = document.getElementById("dataloggerSelector").value;
    window.open("/getDay?day=" + formattedDay + "&datalogger=" + datalogger, "_self");
}


if (data != "") {
    dataArr = data.split("*");
    date = dataArr.pop();
    labelsArr = labels.split(",");

    // Date is in dd/mm/yyy format. Change it to yyy-mm-dd
    year = date.split("/")[2];
    month = date.split("/")[1];
    day = date.split("/")[0];
    normalisedDate = year + "-" + month + "-" + day;

    document.getElementById("dateSelector").value = normalisedDate;

    // Turn data into seperate arrays of humidity, light levels, etc
    var lightLevels = dataArr[1].split(",");
    var humidity = dataArr[3].split(",");
    var temperature = dataArr[5].split(",");
    var phLevel = dataArr[7].split(",");
    var soilMoisture = dataArr[9].split(",");


    drawChart(document.getElementById("lightLevels"), labelsArr, lightLevels, "Light Levels", "#96F3CC", "#BEBBF7");
    drawChart(document.getElementById("humidity"), labelsArr, humidity, "Humidity", "#BEBBF7", "#4EA699");
    drawChart(document.getElementById("temperature"), labelsArr, temperature, "Temperature", "#7772B1", "#A6CEE3");
    drawChart(document.getElementById("phLevel"), labelsArr, phLevel, "PH Level", "#BEBBF7", "#A6CEE3");
    drawChart(document.getElementById("soilMoisture"), labelsArr, soilMoisture, "Soil Moisture", "#7772B1", "#A6CEE3");
} else {
    // Hide the graph
    document.getElementById("graphsRow1").style.display = "none";
    document.getElementById("graphsRow2").style.display = "none";   
    document.getElementById("feedbackText").innerHTML = "Sorry, no data was found for the selected day. Consider changing the day selected to view more data"
}