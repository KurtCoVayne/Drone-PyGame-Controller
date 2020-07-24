import { Schema ,model,Document } from 'mongoose';

const DroneSchema= new Schema({
    name:{ type:String, require: false, default:'New Drone' },
    ready:{ type:Boolean, required:false, default:true },

    initial_pos:{
        type:{ type:String, required:false, default:"Point" },
        coordinates:{ type:[Number], required:false, default:[0,0], index:"2dspheres" }
    },

    goal_pos:{
        type:{ type:String, required:false, default:"Point" },
        coordinates:{ type:[Number], required:false, default:[0,0], index:"2dspheres" }
    },
});

export interface IDrone extends Document{
    name:string,
    ready:boolean,

    initial_pos:{
        type:string,
        coordinates:[number]
    },
    goal_pos:{
        type:string,
        coordinates:[number]
    }
}

export default model<IDrone>('Drones',DroneSchema);