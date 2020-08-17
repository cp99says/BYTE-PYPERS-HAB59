const mongoose=require('mongoose')

const schema=mongoose.Schema({
    
    name:{
        type:String
    },        
    address:{
        type:String
    },
    phoneNumber:{
        type:Number
    },
    time:{
        type:String
    }
})

module.exports=mongoose.model('home_delivery',schema)