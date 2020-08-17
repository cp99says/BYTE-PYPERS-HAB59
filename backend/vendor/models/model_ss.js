const mongoose=require('mongoose')


const schema_ss=mongoose.Schema({
    name:{
        type:String
    },
    contact_number:{
        type:Number
    },
    date:{
        type:String
    },
    time:{
        type:String
    }
})


module.exports=mongoose.model('slots',schema_ss)