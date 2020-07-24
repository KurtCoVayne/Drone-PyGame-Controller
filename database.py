from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
class DatabaseHandler(object):
    def __init__(self,db_conf):
        super().__init__()
        uri = "%s://%s:%s@%s" % (db_conf['Prefix'],
        db_conf['User'], db_conf['Password'], db_conf['Host'])
        self.client = MongoClient(uri)
        self.db = self.client.ignito


    def check(self):
        try:
            self.client.admin.command('ismaster')
        except ConnectionFailure:
            print("Server not available")
            return False
        else:
            return True
        
    def readDroneGoal(self,droneState):
        pass
    def setDroneGoal(self,droneState):
        pass
    """
    return bool whenver drone achieves goal, or if cancels
    """
    def driveDrone(self,goal: Goal) ->bool:
        pass
