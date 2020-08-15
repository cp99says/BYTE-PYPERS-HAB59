$("#customFile").on("change", function () {
  var fileName = $(this).val().replace("C:\\fakepath\\", " ");
  $(this).next(".custom-file-label").html(fileName);
});

// var requestOptions = {
//   method: "GET",
//   redirect: "follow",
// };

// fetch("https://byte-pypers.herokuapp.com/get", requestOptions)
//   .then((response) => response.json())
//   .then((result) => console.log(result))
//   .catch((error) => console.log("error", error));
