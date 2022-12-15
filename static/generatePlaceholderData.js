
// Generates placeholder data
function generatePlaceholderData(numberOfValues) {
    var dataItems = new Array ();

    // f(x)=RandomBetween(1,5) sin(RandomBetween(1,3) x)+((RandomBetween(-5,5))/(10)) x
    for (i=0;i<numberOfValues;i++) {
        var x = i/10
        itemToAppend= Math.random() * (5 - 1) + 1 * Math.sin((Math.random() * (5 - 1) + 1)*x) + (x*(((Math.random() * (5 - -5) + -5))/10))
        dataItems.push(itemToAppend)
    }

    return dataItems

}

function generatePlaceholderLabels(numberOfValues) {
    labels = new Array ();

    for (i=0;i<numberOfValues;i++) {
        labels.push(i)
    }
    return labels
}