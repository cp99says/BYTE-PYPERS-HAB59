const express = require('express')
const app = express();
const mongoose = require('mongoose')
const user = require('./models/model_vendor')
const User=require('./models/model_vendor1')
const multer=require('multer')
const hd=require('./routes/routes')
const ss=require('./routes/routes_ss')
const cors=require('cors')

//    mongoose.connect('mongodb+srv://chetan_mongo:chetan_pwd@cluster0-rdowg.azure.mongodb.net/vendor?retryWrites=true&w=majority', { useNewUrlParser: true, useUnifiedTopology: true, useFindAndModify:false }).then(()=>{
//           console.log('db connected vendor')
//       }).catch(err=>{console.log(err)})


     // mongodb+srv://chetan_mongo:chetan_pwd@cluster0-rdowg.azure.mongodb.net/vendor?retryWrites=true&w=majority

     mongoose.connect('mongodb://localhost:27017/user',{ useNewUrlParser: true, useUnifiedTopology: true, useFindAndModify:false,useCreateIndex:true }).then(()=>{
        console.log('db connected')
    }).catch(err=>{console.log(err)}) 


    //  mongoose.connect('mongodb://localhost:27017/vendor',{ useNewUrlParser: true, useUnifiedTopology: true, useFindAndModify:false,useCreateIndex:true }).then(()=>{
    //      console.log('db connected')
    //  }).catch(err=>{console.log(err)}) 

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
app.use(cors())
app.use('*',cors())
app.use('/hd',hd)
app.use('/ss',ss)

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

app.patch('/patch/:id',uploadUserphoto,async (req,res)=>{       
    
      const newUser = await User.findByIdAndUpdate(req.params.id,req.body)
      res.json({newUser})       

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

    const filterbody=filterObj(req.body)
    if(req.file) filterbody.image=req.file.originalname   

      const newUser = await user.create(filterbody)
      res.json(newUser)
      console.log(req.file)      
})

app.post('/list_items',async (req,res)=>{
    const prod=await User.create(req.body)
    res.status(201).json({
        stock_in_the_shop:prod.length,
        prod
    })
})

app.get('/list_items_get',async (req,res)=>{
    const prod=await User.find()
    res.status(201).json({
        stock_in_the_shop:prod.length,
        prod
    })
})

const port = process.env.PORT || 3000;
app.listen(port, (() => { console.log('server started at port 3000') }))
