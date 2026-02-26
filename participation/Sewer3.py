class Sewer:
    _asset_id: int
    _asset_type: str
    
    def __init__(self, asset_id: int, asset_type: str) -> None:
        self._asset_id = asset_id
        self._asset_type = asset_type
    
    def get_asset_id(self) -> int:
        return self._asset_id
        
    def __str__(self) -> str:
        return "ID: " + str(self._asset_id) + " Type: " + self._asset_type

class WorkOrders:
    emergency_stack:list[Sewer]
    routine_queue:list[Sewer]
    
    def __init__(self):
        self.emergency_stack = []
        self.routine_queue = []
        
    def add_emergency(self, s: Sewer):
        self.emergency_stack.append(s)

    def add_routine(self, s: Sewer):
        self.routine_queue.insert(0, s)

    def handle_next(self):
        if len(self.emergency_stack) > 0: 
            return self.emergency_stack.pop()
        if len(self.routine_queue) > 0:
            return self.routine_queue.pop()
        
        return None

    def pending_jobs(self):
        return len(self.emergency_stack) + len(self.routine_queue)

    def reset(self):
        self.emergency_stack.clear()
        self.routine_queue.clear()

# DON'T CHANGE ANY CODE BELOW THIS LINE
testno = input().strip()

wo = WorkOrders()

if testno == "1":
    wo.reset()
    wo.add_routine(Sewer(1, "CATCHBASIN"))
    wo.add_emergency(Sewer(2, "MANHOLE"))
    wo.add_routine(Sewer(3, "MANHOLE"))
    wo.add_emergency(Sewer(4, "MANHOLE"))

    assert wo.handle_next().get_asset_id() == 4
    assert wo.handle_next().get_asset_id() == 2
    assert wo.handle_next().get_asset_id() == 1
    assert wo.handle_next().get_asset_id() == 3
    print("PASS: Emergency priority logic")

elif testno == "2":
    wo.reset()
    wo.add_routine(Sewer(1, "CATCHBASIN"))
    wo.add_routine(Sewer(2, "CATCHBASIN"))
    wo.add_routine(Sewer(3, "CATCHBASIN"))

    assert wo.handle_next().get_asset_id() == 1
    assert wo.handle_next().get_asset_id() == 2
    assert wo.handle_next().get_asset_id() == 3
    print("PASS: Queue FIFO behavior")

elif testno == "3":
    wo.reset()
    wo.add_emergency(Sewer(1, "CATCHBASIN"))
    wo.add_emergency(Sewer(2, "CATCHBASIN"))
    wo.add_emergency(Sewer(3, "CATCHBASIN"))

    assert wo.handle_next().get_asset_id() == 3
    assert wo.handle_next().get_asset_id() == 2
    assert wo.handle_next().get_asset_id() == 1
    print("PASS: Stack LIFO behavior")





