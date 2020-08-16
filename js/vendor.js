document.getElementById('productSubmit').addEventListener('click', (e) => {
    e.preventDefault();
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    // var name = document.getElementById('prodName').value;
    // var quantity = document.getElementById('prodQuantity').value;
    // var price = document.getElementById('prodPrice').value;

    var raw = JSON.stringify({
        nameOfProduct: document.getElementById('prodName').value,
        quantity: document.getElementById('prodQuantity').value,
        price: document.getElementById('prodPrice').value
    })


    var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
    };

    fetch("https://byte-pypers.herokuapp.com/list_items", requestOptions)
        .then(response => response.text())
        .then(result => {
            alert('Product Added !!');
        }).then(() => {
            document.getElementById('addProd').reset();
        })
        .catch(error => console.log('error', error));
})