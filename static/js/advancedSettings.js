// Set up the functionality for the hamburger menu
hamburgerMenu();
// Fill the datalogger select element with values
fillDataloggerSelectElementWithValues();
// Set up the page
setUpMenuBar(isAdmin);
// If the user is an admin, show pages that are restricted by default
showRestrictedPages(isAdmin);

URLParameters = new URLSearchParams(window.location.search);

// If no parameters are supplied 
// If no start date is supplied, no other paramaters will also be supplied
if (URLParameters.get("start") == null) {
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

    date = year + "-" + month + "-" + day
        
    // Make the start date and end date selector show the date for today
    document.getElementById("startDateSelector").setAttribute("value", date);
    document.getElementById("endDateSelector").setAttribute("value", date);
} else {
    start = URLParameters.get("start");
    end = URLParameters.get("end");

    // Start and end are in dd/mm/yyyy format. Convert them to yyyy-mm-dd
    startDay = start.split("/")[0];
    startMonth = start.split("/")[1];
    startYear = start.split("/")[2];
    startDate = startYear + "-" + startMonth + "-" + startDay;

    endDay = end.split("/")[0];
    endMonth = end.split("/")[1];
    endYear = end.split("/")[2];
    endDate = endYear + "-" + endMonth + "-" + endDay;

    // Make the start date and end date selector show the dates for the data plotted
    document.getElementById("startDateSelector").setAttribute("value", startDate);
    document.getElementById("endDateSelector").setAttribute("value", endDate);
}

// When the load graph button is pressed
function loadGraph() {
    // Find the details needed to dsiplay the graph
    datalogger = document.getElementById("dataloggerSelector").value;
    category = document.getElementById("categorySelector").value;
    startDate = document.getElementById("startDateSelector").value;
    endDate = document.getElementById("endDateSelector").value;

    // Load a the new /advanced-settings? page rather than /advanced-settings and add parameters to make the server return the code
    startDateFormatted = startDate.split("-")[2] + "/" + startDate.split("-")[1] + "/" + startDate.split("-")[0];
    endDateFormatted = endDate.split("-")[2] + "/" + endDate.split("-")[1] + "/" + endDate.split("-")[0];
    window.open("/advanced-settings?datalogger=" + datalogger + "&category=" + category + "&start=" + startDateFormatted + "&end=" + endDateFormatted, "_self");
}

if (data != "") {
    dataArr = data.split(",");
    labelsArr = labels.split(",")

    drawChart(document.getElementById("graph"), labelsArr, dataArr, "Your Data", "#96F3CC", "#BEBBF7");
}  else {
    // Hide the graph
    document.getElementById("graphContainer").style.display = "none";   
    document.getElementById("feedbackText").innerHTML = "Sorry, no data was found for the selected day. Consider changing the day selected to view more data"
}