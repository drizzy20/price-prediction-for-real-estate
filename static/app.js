function onLoadPage() {
  console.log("document loaded");
  var url = "/get_locations"; // URL to fetch locations
  $.get(url, function(data, status) {
    console.log("response for location names approved");
    if (data) {
      var locations = data.locations;
      var uiLocation = document.getElementById("uiLocations");
      $('#uiLocations').empty();
      for (var i in locations) {
        var opt = new Option(locations[i]);
        $('#uiLocations').append(opt);
      }
    }
  });
}

function getBathValue() {
  var uiBathrooms = document.getElementsByName("bath");
  for (var i in uiBathrooms) {
    if (uiBathrooms[i].checked) {
      return parseInt(uiBathrooms[i].value);
    }
  }
  return -1; // Invalid Value
}

function getBHKValue() {
  var uiBHK = document.getElementsByName("bhk");
  for (var i in uiBHK) {
    if (uiBHK[i].checked) {
      return parseInt(uiBHK[i].value);
    }
  }
  return -1; // Invalid Value
}

function onClickedEstimatePrice() {
  console.log("Estimate price button clicked");
  var sqft = document.getElementById("area").value;
  var bhk = getBHKValue();
  var bathrooms = getBathValue();
  var location = document.getElementById("uiLocations").value;
  var estPrice = document.getElementById("predicted-price");

  var url = "/predict_home_price"; // URL to send prediction request

  $.post(
    url,
    {
      total_sqft: sqft,
      location: location,
      bhk: bhk,
      bath: bathrooms
    },
    function(data, status) {
      console.log("response for price prediction received");
      if (data) {
        var price = data.estimated_price;
        estPrice.innerHTML = "Predicted Price: " + price;
      }
    }
  );
}

// Wait for the DOM to load
document.addEventListener("DOMContentLoaded", function() {
  // Get the "Predict Price" button
  var predictButton = document.getElementById("predict-btn");

  // Add the click event listener
  predictButton.addEventListener("click", onClickedEstimatePrice);

  // Call the onLoadPage function to fetch locations
  onLoadPage();
});
