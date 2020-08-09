const mongoose=require('mongoose');


const schema=new mongoose.Schema({
    nameOfProduct:{
        type:String,
        required:[true,'User must enter the name of product']
    },
    quantity:{
        type:Number,
        required:[true,'User must enter the quantity of product']
    },
    price:{
        type:Number,
        required:[true,'User must enter the price of product']
    }
})

// module.exports=mongoose.model('user_data',schema)

const User=mongoose.model('user_data',schema)
module.exports=User;