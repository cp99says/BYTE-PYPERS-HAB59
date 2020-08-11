const mongoose=require('mongoose');

const schema= mongoose.Schema({
    image:{
        type:String,
        required:[true,'user must enter an image of product']
    },
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

module.exports=mongoose.model('vendor',schema)