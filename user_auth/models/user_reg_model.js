const mongoose = require('mongoose')
const validator = require('validator')
const bcrypt = require('bcryptjs')

const schema = mongoose.Schema({
    name: {
        type: String
    },
    email: {
        type: String,        
        validate: [validator.isEmail, 'Email is invalid Please provide a valid email']
    },
    password: {
        type: String,
        select:false
    },
    passwordConfirm: {
        type: String,
        validate: {
            validator: function (el) {
                return el === this.password
            },
            message: `password and passwordConfirm aren't same`
        }
    }
})
schema.pre('save', async function (next) {
    this.password = await bcrypt.hash(this.password, 10)
    this.passwordConfirm=undefined
    next();

})

schema.methods.correctPassword= async function(candidatePassword, userPassword){
    return await bcrypt.compare(candidatePassword,userPassword)
}

module.exports = mongoose.model('user_reg', schema)