const mongoose=require('mongoose')

const schema=mongoose.Schema({
    address:{
        type:String
    },
    phoneNumber:{
        type:Number
    }
})

module.exports=mongoose.model('home_delivery',schema)