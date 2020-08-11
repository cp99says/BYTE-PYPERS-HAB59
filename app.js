const express = require('express')
const app = express();
const mongoose = require('mongoose')
const User = require('./model')
const multer=require('multer')

const multerStorage=multer.diskStorage({
    destination:(req,file,cb)=>{
        cb(null,'images');
    },
    filename:(req,file,cb)=>{
       
        cb(null,`${file.originalname}`)
    }
})

const upload=multer({
      storage:multerStorage

})
const uploadUserphoto=upload.single('image')
app.use(express.json())
mongoose.connect('mongodb://localhost:27017', { useNewUrlParser: true, useUnifiedTopology: true, useFindAndModify:false }).then(()=>{
    console.log('db connected')
}).catch(err=>{console.log(err)})

const filterObj = (obj, ...allowedFields) => {
    const newObj = {};
    Object.keys(obj).forEach(el => {
      if (allowedFields.includes(el)) newObj[el] = obj[el];
    });
    return newObj;
  };

app.get('/get', async (req,res)=>{
    const vendor=await User.find();
    res.status(200).json({
        no_of_items:vendor.length,
        vendor
    })
})
// app.post('/post',async (req, res) => {


//     const filterbody=filterObj(req.body,'nameOfProduct','quantity','price')
//     if(req.file) filterbody.image=req.file.originalname   
   
//        const a=await User.create(filterbody)
//     //    console.log(a)
//        res.status(201).json(a)       
    
   
// })

app.patch('/patch/:id',uploadUserphoto,async (req,res)=>{
       
    
      const newUser = await User.findByIdAndUpdate(req.params.id,req.body)
      res.json({newUser})
       console.log(req.file)
       console.log(req.body)  

})
    

app.delete('/delete/:id',async (req,res)=>{
    try{
        await User.findByIdAndDelete(req.params.id)
        res.status(203).json({
            status:'success',
            message:'data deleted'
        })
    }
    catch(err){
        res.json(404).json(err)
    }

})

app.post('/imagee',uploadUserphoto,async(req,res)=>{


    const filterbody=filterObj(req.body,'nameOfProduct','quantity','price')
    if(req.file) filterbody.image=req.file.originalname   

      const newUser = await User.create(filterbody)
      res.json(newUser)
      console.log(req.file)
      console.log(req.body)  

})

app.listen(3000, (() => { console.log('server started at port 3500') }))
