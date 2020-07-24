import { Resolver } from 'dns';
import { Router, Response } from 'express';
import { droneControllers } from '../controllers/drone.controllers';
const router = Router();

router.post('/add', droneControllers.add);

router.delete('/remove', droneControllers.remove);

router.get('/get', droneControllers.get);

router.put('/edit', droneControllers.edit);

export default router;