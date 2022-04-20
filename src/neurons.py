from random import randint
class Neurons():
    def __init__(self):
        self.age
        self.direction={
            0:"N",
            1:"NE",
            2:"E",
            3:"EW",
            4:"W",
            5:"WS",
            6:"S",
            7:"SE",
        }
        self.current=randint(0,7)

class ActionNeurons():
    def __init__(self,):
        self.age=0
        self.move_random=None
        
        self.move_left=None
        self.move_right=None
        self.move_forward=None
        self.move_backward=None

        self.move_east=None
        self.move_west=None
        self.move_north=None
        self.move_south=None
        

class SensorNeurons():
    def __init__(self,):
        self.age=0

class InnerNeurons():
    def __init__(self,):
        self.age=0
