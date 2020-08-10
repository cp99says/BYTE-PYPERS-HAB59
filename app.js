const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const multer = require('multer');
const GridFsStorage = require('multer-gridfs-storage');
const Grid = require('gridfs-stream');
const app = express();
const posts=require('./posts') 



//middleware
app.use(express.json())
// app.use(bodyParser.json())
app.set('view engine', 'ejs')
app.use('/post',posts)

// const mongoURI = ();
const conn = mongoose.createConnection('mongodb://localhost:27017', { useNewUrlParser: true, useUnifiedTopology: true })

app.get('/', (req, res) => {
  res.render('index')
})

let gfs;
conn.once('open', function () {
    gfs = Grid(conn.db, mongoose.mongo);
    gfs.collection('uploads')
})  
const storage = new GridFsStorage({
     url: 'mongodb://localhost:27017',
    // url:'mongodb+srv://chetan_mongo:chetan_pwd@cluster0-rdowg.azure.mongodb.net/<dbname>?retryWrites=true&w=majority',
    file: (req, file) => {
        return new Promise((resolve, reject) => {

            const filename = (file.originalname);
            const fileInfo = {
                filename: filename,
                bucketName: 'uploads'
            };
            resolve(fileInfo);
        });
    }
})
const upload = multer({ storage });



app.post('/upload', upload.single('file'), (req, res) => {
    // const data=await user.create(req.body)
    //const dtaa=user.create({req.body})
    
    res.json({
        file: req.file,
       
    })
})


// app.post('/upload',(req,res)=>{

// })

//@route -get, it display all the data 
app.get('/files', (req, res) => {
    gfs.files.find().toArray((err, files) => {
        // Check if files
        if (!files || files.length === 0) {
            return res.status(404).json({
                err: 'No files exist'
            });
        }
        // Files exist
        return res.json({
          number_of_entries:files.length,
          files
        });
    });
});

app.get('/image/:filename', (req, res) => {
    gfs.files.findOne({ filename: req.params.filename }, (err, file) => {
      // Check if file
      if (!file || file.length === 0) {
        return res.status(404).json({
          err: 'No file exists'
        });
      }
  
      // Check if image
      if (file) {
        // Read output to browser
        const readstream = gfs.createReadStream(file.filename);
        readstream.pipe(res);
      } else {
        res.status(404).json({
          err: 'Not an image'
        });
      }
    });
  });

//   app.get('/image1', (req, res) => {
//     gfs.files.find().toArray((err, files) => {
//       // Check if files
//       if (!files || files.length === 0) {
//           return res.status(404).json({
//               err: 'No files exist'
//           });
//       }
//       else
//       {
//         files.map(file=>{
//           if(files.contentType === 'image/jpeg' || image === 'image/png')
//           {
//             file.isImage=true
//           }
//           else{
//             file.isImage=false
//           }
//         })
//         res.render('index',{files:files})
//       }
//   });
// })

const port = 3000
app.listen(port, '127.0.0.1', () => { console.log(`server started at port: ${port}`) })