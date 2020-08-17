const express=require('express')
const app=express();
const ss=require('./../models/model_ss')
const mongoose=require('mongoose')


app.post('/post_ss',async (req,res)=>{
    const sst=await ss.create(req.body)
    res.status(202).json({        
        customer_slot:sst        
    })        
})

app.get('/get_ss',async (req,res)=>{
    const sst=await ss.find()
    res.status(202).json({        
        customer_slot:sst.length,
        data:sst        
    })        
})


module.exports=app;