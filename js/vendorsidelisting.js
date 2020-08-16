var requestOptions = {
    method: 'GET',
    redirect: 'follow'
};

var dynamicListing = document.getElementById('currentListing');

function hideSpinnerE() {
    document.getElementById('spinnerDelivery').style.display = 'none';
}

fetch("https://byte-pypers.herokuapp.com/list_items_get", requestOptions)
    .then(response => response.text())
    .then(result => {
        hideSpinnerE();
        var listingResult = JSON.parse(result);
        console.log(listingResult.prod);
        var delbtnlength = listingResult.prod.length;

        for (var i = 0; i < listingResult.prod.length; i++) {
            var name = listingResult.prod[i].nameOfProduct;
            var price = listingResult.prod[i].price;
            var quantity = listingResult.prod[i].quantity;
            console.log(name)
            console.log(price)
            console.log(quantity)

            var listingContent = `<tbody><tr id="list${i+1}"><th scope="row">${i+1}</th><td>${name}</td><td>${quantity}</td><td>${price}</td><td><button type="button" class="btn btn-primary" data-toggle="modal" data-target="#exampleModal">Drop Price</button></td><td><button type="button" class="btn btn-danger" id="${i+1}">Delete Item</button></td></tr></tbody>`

            dynamicListing.insertAdjacentHTML('beforeend', listingContent);

        }
        return delbtnlength;
    })
    .catch(error => console.log('error', error));