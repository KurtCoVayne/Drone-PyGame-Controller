import { Request, Response } from 'express';
import DroneModel,{IDrone} from '../models/drone.model';

class DroneControllers{

    public async add(req:Request,res:Response){
        const {name,initial_pos,goal_pos} = req.body;

        const newDrone:IDrone= new DroneModel({
            name,initial_pos,goal_pos
        });
        await newDrone.save();
        
        return res.json({message:'done'});
    }

    public async edit(req:Request,res:Response){
        const {id,name,ready,initial_pos,goal_pos} = req.body;
        const drone = await DroneModel.findById(id);

        if(!drone) return res.json({message:'DroneNotFound'}).status(404);

        if(name!=undefined || name!=null) drone.name=name;
        if(ready!=undefined || ready!=null) drone.ready=ready;
        if(initial_pos!=undefined || initial_pos!=null) drone.initial_pos.coordinates=initial_pos;
        if(goal_pos!=undefined || goal_pos!=null) drone.goal_pos.coordinates=goal_pos;

        await drone.save();

        return res.json({message:'done'});
    }

    public async get(req:Request,res:Response){
        const {id} = req.body;
        const drone = await DroneModel.findById(id);

        return res.json({message:'done',drone});
    }

    public async remove(req:Request,res:Response){
        const {id} = req.body;
        const drone = await DroneModel.findByIdAndRemove(id);
        return res.json({message:'done'});
    }

}

export const droneControllers= new DroneControllers();