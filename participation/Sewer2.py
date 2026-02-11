class Asset:

    def maintenance_cost(self) -> float:
        return 50


class Sewer(Asset):
    _asset_id: int
    _asset_type: str
    _lon: float
    _lat: float
    _priority: int
    
    asset_count: int = 0

    def __init__(self, asset_id: int, asset_type: str, lon: float, lat: float, priority: int) -> None:
        self._asset_id = asset_id
        self._asset_type = asset_type
        self._priority = priority
        Sewer.asset_count += 1

        is_valid = Sewer.valid_coordinates(lon, lat)
        if is_valid:
            self._lat = lat
            self._lon = lon
        else:
            raise ValueError
        
    def maintenance_cost(self):
        return super().maintenance_cost() + 25
         
    @staticmethod
    def valid_coordinates(lon: float, lat: float) -> bool:
        return 43 < lat < 44 and 79 < lon < 80    
            
    def __str__(self) -> str:
        return "ID: " + str(self._asset_id) + " Type: " + self._asset_type


# DON'T CHANGE ANY CODE BELOW THIS LINE
testno = input().strip()

if testno == "1":
    # Test static attribute asset_count
    s1 = Sewer(1, "CATCHBASIN", 79.5, 43.5, 0)
    s2 = Sewer(2, "MANHOLE", 79.6, 43.6, 1)
    print(Sewer.asset_count)

elif testno == "2":
    # Test static method valid_coordinates
    print(Sewer.valid_coordinates(79.5, 43.5))   # should be True
    print(Sewer.valid_coordinates(81.0, 43.5))   # should be False

elif testno == "3":
    # Test constructor raising ValueError for invalid coordinates
    try:
        s = Sewer(3, "CATCHBASIN", 100.0, 20.0, 0)
        print("NO ERROR")
    except ValueError:
        print("VALUE ERROR")

elif testno == "4":
    # Test overridden maintenance_cost
    s = Sewer(4, "MANHOLE", 79.7, 43.7, 2)
    print(s.maintenance_cost())

