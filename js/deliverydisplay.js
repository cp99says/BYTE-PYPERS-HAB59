var requestOptions = {
    method: 'GET',
    redirect: 'follow'
};


var dynamic = document.getElementById('deliveryDynamic');
console.log(dynamic);

function hideSpinnerD() {
    document.getElementById('spinnerDelivery').style.display = 'none';
}

fetch("https://byte-pypers.herokuapp.com/hd/display_deliveries", requestOptions)
    .then(response => response.text())
    .then(result => {
        hideSpinnerD();
        var deliveryResult = JSON.parse(result);
        console.log(deliveryResult.data)

        var length = deliveryResult.data.length;

        for (i = 0; i < length; i++) {

            var name, mobile, address, time;
            name = deliveryResult.data[i].name;
            mobile = deliveryResult.data[i].phoneNumber;
            time = deliveryResult.data[i].time;
            address = deliveryResult.data[i].address;
            console.log(name);
            console.log(mobile);
            console.log(time);
            console.log(address);


            var content = `<tbody><tr><th scope="row">${i+1}</th><td>${name}</td><td>${mobile}</td><td>${address}</td><td>${time}</td><td class="text-center"><div class="btn-group" role="group" aria-label="Basic example"><button type="button" class="btn btn-success" id="accept">Accept</button><button type="button" class="btn btn-danger" id="decline">Decline</button></div></td></tr></tbody>`

            dynamic.insertAdjacentHTML('beforeend', content);
        }

    }).then(() => {
        var acceptBtn = document.querySelectorAll('#accept');
        var declineBtn = document.querySelectorAll('#decline');
        var acceptArr = Array.from(acceptBtn);
        var declineArr = Array.from(declineBtn);
        console.log(acceptArr);
        console.log(declineArr);


        acceptBtn.forEach((e) => {
            e.addEventListener('click', () => {
                if (e.innerHTML === "Accept") {
                    e.innerHTML = "Accepted";
                }
            })
        })

        declineBtn.forEach((f) => {
            f.addEventListener('click', () => {
                if (f.innerHTML === "Decline") {
                    f.innerHTML = "Declined";
                }
            })
        })




    })
    .catch(error => console.log('error', error));