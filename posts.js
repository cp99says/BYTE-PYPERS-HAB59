const express = require('express')
const app = express()
const user = require('./model')
app.use(express.json())

app.get('/get', async (req,res)=>{
    const vendor=await User.find();
    res.status(200).json({
        no_of_items:vendor.length,
        vendor
    })
})

app.post('/post',async (req, res) => {
    try {
       const a=await User.create(req.body)
    //    console.log(a)
       res.status(201).json(a)       
    }
    catch (err) {
        res.json({
            err
        })
    }
})

app.patch('/patch/:id',async (req,res)=>{
    try {
        
        const updated_data = await User.findByIdAndUpdate(req.params.id, req.body, {
          new: true,
          runValidators: true
        });
    
        res.status(200).json({
          status: 'success',
          data: {
            updated_data
          }
        });
      } catch (err) {
        res.status(404).json({
          status: 'fail',
          message: err
        });
      }
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



module.exports = app;