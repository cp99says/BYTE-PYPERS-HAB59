$("#customFile").on("change", function() {
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

// var myHeaders = new Headers();
// myHeaders.append("Content-Type", "application/json");

// var raw = JSON.stringify({ email: "asd@gmail.com", password: "abc@123456" });

// var requestOptions = {
//   method: "POST",
//   headers: myHeaders,
//   body: raw,
//   redirect: "follow",
// };

// fetch("https://byte-pypers-auth.herokuapp.com/customer/login", requestOptions)
//   .then((response) => response.text())
//   .then((result) => console.log(result))
//   .catch((error) => console.log("error", error));




// var myHeaders = new Headers();
// myHeaders.append("Content-Type", "application/json");

// var raw = JSON.stringify({
//     name: "atimabh test 2",
//     contact_number: "8802216912",
//     date: "15/07/20",
//     time: "04:00 P.M.",
// });

// var requestOptions = {
//     method: "POST",
//     headers: myHeaders,
//     body: raw,
//     redirect: "follow",
// };

// fetch(
//         "https://byte-pypers-auth.herokuapp.com/customer/select_slot",
//         requestOptions
//     )
//     .then((response) => response.text())
//     .then((result) => console.log(result))
//     .catch((error) => console.log("error", error));