document.getElementById("slotSubmit").addEventListener('click', () => {

    var raw = JSON.stringify({
        name: document.getElementById("slotName").value,
        contact_number: document.getElementById("slotMobile").value,
        date: document.getElementById("slotDate").value,
        time: document.getElementById("slotTime").value
    });

    var myHeaders = new Headers();
    myHeaders.append("Accept", "application/json");
    myHeaders.append("Content-Type", "application/json");

    console.log(raw);

    var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
    };

    fetch("https://byte-pypers-auth.herokuapp.com/customer/select_slot", requestOptions)
        .then(response => response.text())
        .then(result => console.log(result))
        .then(alert('Slot Successfully Booked'))
        .then(() => {
            location.reload();
            document.getElementById('pickup').reset();
        })
        .catch(error => console.log('error', error));
});