from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import pprint
class DatabaseHandler(object):
    def __init__(self,drone_id,db_conf):
        super().__init__()
        uri = uri = f"{db_conf['Prefix']}://{db_conf['User']}:{db_conf['Password']}@{db_conf['Host']}"
        self.client = MongoClient(uri)
        self.db = self.client.ignito_realtime
        self.id = drone_id


    def check(self):
        try:
            self.client.admin.command('ismaster')
        except ConnectionFailure:
            print("Server not available")
            return False
        else:
            return True
    
    def getDrone(self):
        drone = db.find_one({"_id":self.id})
        pprint(drone)
        return drone

    def setDrone(self,droneState):
        pass
    def setGoalGeoCoord(self, geoCoord: GeoCoord) -> Drone:
        return getDrone()

    """
    The actual use of this function is to get the db if a custom query is needed
    """
    def getDB(self,droneState):
        return self.db
    """
    return bool whenver drone achieves goal, or if cancels
    """
