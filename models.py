import math
class GeoCoord:
    def __init__(self,lat,lon,altitude):
        super().__init__()
        self.lat = lat
        self.lon = lon
        self.altitude = altitude
    def __add__(self,offsets):
        print(f"adding {offsets}")
        assert len(offsets) == 3, f"3 numbers needed given {len(offsets)}"
        dx,dy,dz = offsets

        self.lat = self.lat + (180/math.pi)*(dy/6378137)
        self.lon = self.lon + (180/math.pi)*(dx/6378137)/math.cos(self.lon)
        self.altitude = self.altitude +dz

        return self
    def __str__(self):
        return f"lat: {self.lat}, lon: {self.lon}, altitude: {self.altitude}"

if __name__ == "__main__":
    g = GeoCoord(0,0,0)
    print(g)
    x = g + (1,2,3)
    print(x)
