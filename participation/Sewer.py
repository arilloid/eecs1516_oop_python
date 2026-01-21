
class Sewer:
    _asset_id: int
    _asset_type: str
    _lon: float
    _lat: float
    _priority: int

    def __init__(self, asset_id: int, asset_type: str, lon: float, lat: float, priority: int) -> None:
        self._asset_id = asset_id
        self._asset_type = asset_type
        self._lon = lon
        self._lat = lat
        self._priority = priority

    @property
    def priority(self) -> int:
        return self._priority

    @property
    def asset_id(self) -> int:
        return self._asset_id

    def change_id(self, new_id: int) -> None:
        self._asset_id = new_id

    def __str__(self) -> str:
        return "ID: " + str(self._asset_id) + " Type: " + self._asset_type


class MaintainanceWorker:
    _userid: int
    _name: str
    _todolist: list[Sewer]

    def __init__(self, id: int, name: str):
        self._userid = id
        self._name = name
        self._todolist = []

    def add_todo(self, sewer: Sewer) -> None:
        if sewer.priority > 0: self._todolist.append(sewer)

    def high_priority_todos(self, min_priority: int) -> list[Sewer]:
        return [s for s in self._todolist if s.priority > min_priority]
    
    def __str__(self) -> str:
        return "USER ID: " + str(self._userid) + " NAME: " + self._name + " TODOS: " + str(
            [str(s) for s in self._todolist]) + "\n"


# DON'T CHANGE ANY CODE BELOW THIS LINE
testno = input().strip()
s0 = Sewer(8, 'CATCHBASIN', 49, 79, 0)
s1 = Sewer(8, 'CATCHBASIN', 49, 79, 1)
s2 = Sewer(9, 'MANHOLE', 48, 79, 2)
m = MaintainanceWorker(1, "Javier")
m.add_todo(s0)
m.add_todo(s1)
m.add_todo(s2)

if testno == '1':
    s1.change_id(6)
    print(s1)
elif testno == '2':
    print(m)
else:
    print([str(s) for s in m.high_priority_todos(1)])