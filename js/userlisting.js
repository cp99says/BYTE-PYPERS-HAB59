var requestOptions = {
    method: 'GET',
    redirect: 'follow'
};

var userDynamic = document.getElementById('userStore');

function hideSpinner() {
    document.getElementById('spinnerDelivery').style.display = 'none';
}

fetch("https://byte-pypers.herokuapp.com/list_items_get", requestOptions)
    .then(response => response.text())
    .then(result => {
        hideSpinner();
        var userResult = JSON.parse(result);
        console.log(userResult.prod)

        for (var i = 0; i < userResult.prod.length; i++) {
            var listName = userResult.prod[i].nameOfProduct;
            var listPrice = userResult.prod[i].price;
            var listQuant = userResult.prod[i].quantity;
            console.log(listName)
            console.log(listPrice)
            console.log(listQuant)

            var userContent = ` <div class="card mb-3 cardWrapper shadow"><div class="row no-gutters"><div class="col-md-4"><img src="images/product.svg" class="card-img" alt="..."></div><div class="col-md-8"><div class="card-body"><div class="prodName"><h5 class="card-title">${listName}</h5><p class="card-text price">MRP: <i class="fas fa-rupee-sign"></i> ${listPrice}</p><p class="card-text"><small class="text-muted">Quantity Available : ${listQuant}</small></p></div><div class="prodSelect"><select class="custom-select mr-sm-2" id="inlineFormCustomSelect"><option selected>Quantity</option><option value="1">1</option><option value="2">2</option><option value="3">3</option><option value="3">4</option><option value="3">5</option></select><div class="custom-control custom-checkbox"><input type="checkbox" class="custom-control-input" id="customCheck${i+1}"><label class="custom-control-label" for="customCheck${i+1}">Add to Cart</label></div></div></div></div></div></div>`

            userDynamic.insertAdjacentHTML('beforeend', userContent);
        }

    })
    .catch(error => console.log('error', error));