const express = require('express')
const app = express();
const mongoose = require('mongoose')
const cors=require('cors')
const reg=require('./routes/user_reg')

      mongoose.connect('mongodb://localhost:27017/user', {useNewUrlParser: true, useUnifiedTopology: true, useFindAndModify:false}).then(()=>{
                   console.log('db connected')
               }).catch(err=>{console.log(err)})
    


    //    mongoose.connect('mongodb+srv://chetan_mongo:chetan_pwd@cluster0-rdowg.azure.mongodb.net/user?retryWrites=true&w=majority', { useNewUrlParser: true, useUnifiedTopology: true, useFindAndModify:false }).then(()=>{
    //           console.log('db connected')
    //       }).catch(err=>{console.log(err)})


app.use(express.json())
app.use(cors())
app.use('*',cors())   
app.use('/customer',reg)

const port = process.env.PORT || 4500;
app.listen(port, (() => { console.log('server started at port 4500') }))
