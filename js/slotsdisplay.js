var requestOptions = {
    method: 'GET',
    redirect: 'follow'
};

function hideSpinner() {
    document.getElementById('spinner').style.display = 'none';
}

fetch("https://byte-pypers-auth.herokuapp.com/customer/display_slot", requestOptions)
    .then(response => response.text())
    .then(result => {
        hideSpinner();
        var slotResult = JSON.parse(result);
        console.log(slotResult)

        var tableLength = slotResult.data.length;

        var dynamic = document.getElementById("dyanmicSlots");
        for (i = 0; i < tableLength; i++) {

            var names, mobiles, dates, times;
            names = slotResult.data[i].name;
            mobiles = slotResult.data[i].contact_number;
            dates = slotResult.data[i].date;
            times = slotResult.data[i].time;
            console.log(names);
            console.log(mobiles);
            console.log(dates);
            console.log(times);



            var content = `<tbody><tr><th scope="row">${i+1}</th><td>${names}</td><td>${mobiles}</td><td>${dates}</td><td>${times}</td></tr></tbody>`
            dynamic.insertAdjacentHTML('beforeend', content);

        }




    })
    .catch(error => console.log('error', error));