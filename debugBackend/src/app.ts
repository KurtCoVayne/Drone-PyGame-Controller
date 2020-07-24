import express,{Application} from 'express';
import mongoose from 'mongoose';
import morgan from 'morgan';
import session from 'express-session';
import cors from 'cors';
import DroneRoutes from './routes/drone.routes';
import bodyParser from 'body-parser';

/* Initializations */
const app:Application=express();
if(process.env.NODE_ENV === 'dev') require('dotenv').config();

/* Middlewares */
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended:false}));
app.use(morgan('dev'));
app.use(cors());

/* Routes */
app.use('/',DroneRoutes);

/* DB and server setup */
mongoose.connect('mongodb://localhost:27017/test',{ useNewUrlParser: true,useUnifiedTopology: true }, (err) => {
    if (err) throw err;
    console.log('DB connected');
});
app.listen(9000, () => {
    console.log(`Server running in port ${9000}`);
});
console.log(`Server running in mode ${process.env.NODE_ENV}`);