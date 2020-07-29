import { Resolver } from 'dns';
import { Router, Response } from 'express';
import { droneControllers } from '../controllers/drone.controllers';
const router = Router();
import multer from 'multer';
const upload = multer();

router.post('/add', upload.fields([]), droneControllers.add);

router.delete('/remove', upload.fields([]), droneControllers.remove);

router.get('/get', upload.fields([]), droneControllers.get);

router.put('/edit', upload.fields([]), droneControllers.edit);

export default router;