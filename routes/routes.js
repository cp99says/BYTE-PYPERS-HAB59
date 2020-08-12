const express = require('express')
const app = express();
const homeDel = require('../models/model_homedelivery')


app.get('/display_deliveries',async (req, res) => {
    const data = await homeDel.find();
    res.status(203).json({
        number_of_deliveries: data.length,
        data
    })
})

app.post('/set_home_delivery', async (req, res) => {
    const hd = await homeDel.create(req.body);
    res.status(203).json({
        hd
    })
})


module.exports = app