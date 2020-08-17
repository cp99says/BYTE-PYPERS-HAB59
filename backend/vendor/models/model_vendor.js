const mongoose=require('mongoose');

const schema= mongoose.Schema({
    image:{
        type:String,
        required:[true,'user must enter an image of product']
    }
    
})

// module.exports=mongoose.model('user_data',schema)

module.exports=mongoose.model('vendor',schema)