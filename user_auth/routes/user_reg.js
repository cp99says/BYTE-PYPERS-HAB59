const express = require('express')
const app = express();
const cors = require('cors')
const reg_model = require('../models/user_reg_model')
const jwt = require('jsonwebtoken')
const bcrypt=require('bcryptjs')
const mongoose=require('mongoose')
   
app.post('/signup', async (req, res) => {
    try {        
        const user = await reg_model.create(req.body)
        const token=jwt.sign({id:user._id},'super-secret',{expiresIn:'30d'})
        res.status(201).json({
            status: 'user registered successfully',
            data: user,
            token
        })
    }
    catch (err) {
        res.status(401).json({
            err
        })
        }
});

app.post('/login', async (req,res)=>{
  const {email,password} = req.body
  if(!email || !password) res.send('please enter email and password')

 const user = await reg_model.findOne({email}).select('+password')
 
 //const correct=await reg_model.correctPassword(password,user.password)
 const a=await bcrypt.compare(password,user.password)
 if(email===user.email && a)
 {
     res.status(201).json({
         status:'success',
         message:'You have logged in successfuly'
     })
 }
 else if(email!==user.email || !a){
    res.status(401).json({
        status:'failure',
        message:'Incorrect email id or password combination'
    })
 }

 })
//  if(!user || !correct)
//  {
//      res.send('there is error');
//  }
 



module.exports = app;
