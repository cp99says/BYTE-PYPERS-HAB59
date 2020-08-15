const prodBtn = document.getElementById('productSubmit')
prodBtn.addEventListener('click', (e) => {
    e.preventDefault();
    var imageLoc = document.getElementById('imgupload').value;
    console.log(imageLoc);
    var productName = document.getElementById('prodName').value;
    console.log(productName);
    var productQuant = document.getElementById('prodQuantity').value;
    console.log(productQuant);
    var productPrice = document.getElementById('prodPrice').value;
    console.log(productPrice);
    var formdata = new FormData();
    formdata.append(
        "image", imageLoc
    );
    formdata.append("nameOfProduct", productName);
    formdata.append("quantity", productQuant);
    formdata.append("price", productPrice);

    var requestOptions = {
        method: "POST",
        body: formdata,
        redirect: "follow",
    };

    fetch("https://byte-pypers.herokuapp.com/imagee", requestOptions)
        .then((response) => response.text())
        .then((result) => console.log(result))
        .catch((error) => console.log("error", error));
});