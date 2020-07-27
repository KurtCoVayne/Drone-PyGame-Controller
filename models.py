import math
class GeoCoord:
    def __init__(self,lat,lon,alt):
        super().__init__()
        self.lat = lat
        self.lon = lon
        self.alt = alt
    def __add__(self,offsets):
        print(f"adding {offsets}")
        assert len(offsets) == 3, f"lat,lon,alt needed; given {len(offsets)}"
        dx,dy,dz = offsets

        self.lat = self.lat + (180/math.pi)*(dy/6378137)
        self.lon = self.lon + (180/math.pi)*(dx/6378137)/math.cos(math.radians(self.lon))
        self.alt = self.alt + dz

        return self
    def __str__(self):
        return f"lat: {self.lat}, lon: {self.lon}, alt: {self.alt}"

if __name__ == "__main__":
    g = GeoCoord(0,0,0)
    print(g)
    x = g + (1,2,3)
    print(x)
