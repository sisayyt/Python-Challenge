// from data.js
var tableData = data;

// YOUR CODE HERE!
// Use D3 to select the table
var table = d3.select("table");
console.log(data)

// selecting table boday using D3
var tbody = d3.select("tbody");

// Use d3 to create a bootstrap striped table
// http://getbootstrap.com/docs/3.3/css/#tables-striped
table.attr("class", "table table-striped");

// Append one table row `tr` to the table body
var row = tbody.append("tr");

//Creating the function that provided the data to the table
function buildTable(tableData) {
    tbody.html("");
    //Looping through the data to get the elements using forEach funtion
    tableData.forEach((ufoCitings) => {
            console.log(ufoCitings);
            var row = tbody.append("tr");
    //Enter each row in the table
        Object.entries(ufoCitings).forEach(([key, value]) => {
            console.log(`key = ${key} and value ${value}`);
            var cell = row.append('td');
            cell.text(value);
        });
    });
}


// Input elements -- building the data in console.log
   var tableData = buildTable(tableData);
    console.log(tableData);

// Filtering and enetring the data using the submitt button
    var submit = d3.select("#filter-btn");
    console.log(submit);

      // Get the value property of the input element
    var inputDate = d3.select("#datetime");
    var inputCity = d3.select("#city");
    var inputState = d3.select("#state");
    var inputCountry = d3.select("#country");
    var inputShape = d3.select("#shape");
    var inputDuration = d3.select("#duration");
    var inputComments = d3.select("#comments");


// Using the `on` function in d3 to attach an event to the handler function
    submit.on("click", function() {

 // Prevent the page from refreshing
    d3.event.preventDefault();

// Getting the value property of the input element
    var inputValue = inputDate.property("value");
    console.log(inputValue);
    console.log(tableData);
// Creating filtered dataset based on InputValue entered by user
    var tableDataFiltered = data.filter(ufoRecord => ufoRecord.datetime === inputValue);
    console.log(tableDataFiltered);
  
//  Building new UFO Table with the filtered subset of UFO Sighting data
    buildTable(tableDataFiltered);
 
});