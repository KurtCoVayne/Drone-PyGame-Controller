from dronekit import connect

class Goal(object):
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
class DroneHandler(object):
    def __init__(self, drone_conf):
        super().__init__()
        connection_string = drone_conf['ConnectionString']
        baud = drone_conf['BaudRate']
        if drone_conf['SITL'] == 'True':
            import dronekit_sitl
            sitl = dronekit_sitl.start_default()
            connection_string = sitl.connection_string()

        self.vehicle = connect(connection_string, baud=baud, wait_ready=True)

    def check(self):
        try:
            self.vehicle.version()
        except Exception as e:
            print(str(e))
            return False
        else:
            return True and self.vehicle.is_armable()
        
    def setSpeed(self,speed):
        pass
    def setGoal(self,goal):
        pass