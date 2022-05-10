from random import randint

from coordinate import Coordinate
# class Direction():
#     directions={
#         "N":0,
#     }

class Compass():
    '''
    Compass direction

    7 0 1
      ^
      |
    6 x 2
    
    5 4 3

    from x the direction is calculated

    '''
    # Current Direction INDEPENDENT
    DIRECTIONS={
        "N": 0,
        "NE": 1,
        "E": 2,
        "SE": 3,
        "S": 4,
        "WS": 5,
        "W": 6,
        "NW": 7,
    }
    NORTH = 0,
    NORTHEAST = 1,
    EAST = 2,
    SOUTHEAST = 3,
    SOUTH = 4,
    WESTSOUTH = 5,
    WEST = 6,
    NORTHWEST = 7,

    # Current Direction DEPENDENT
    FRONT=0
    FRONTRIGHT=1
    RIGHT=2
    BACKRIGHT=3
    BACK=4
    BACKLEFT=5
    LEFT=6
    FRONTLEFT=7
    
    def __init__(self,current:int=None):
        if(current==None):
            self.current=randint(0,7)
        else:
            self.current=current
    
    def rotate(self,__direction)->int:
        '''return rotated direction based on current direction'''
        return (self.current+__direction)%len(Compass.DIRECTIONS)

    def turn(self,__direction:int)->None:
        '''inplace turns the direction'''
        self.current=self.rotate(__direction)
    
    def direction(self)->str:
        '''direction of compass'''
        return Compass.DIRECTIONS[self.current]

    def getNextLocation(self,__currentlocation:Coordinate,__direction:int,dependency:bool=True)->Coordinate:
        '''if dependency on current direction is ture
        
        return next location based on given direction form current direction 
        
        else 
        
        return next location independent of current direction'''
        dir=__direction
        if(dependency):
            dir=self.rotate(__direction)

        if(dir==0):
            return __currentlocation+Coordinate(0,1)
        if(dir==1):
            return __currentlocation+Coordinate(1,1)
        if(dir==2):
            return __currentlocation+Coordinate(1,0)
        if(dir==3):
            return __currentlocation+Coordinate(1,-1)
        if(dir==4):
            return __currentlocation+Coordinate(0,-1)
        if(dir==5):
            return __currentlocation+Coordinate(-1,-1)
        if(dir==6):
            return __currentlocation+Coordinate(-1,0)
        if(dir==7):
            return __currentlocation+Coordinate(-1,1)

    def __str__(self) -> str:
        return "Current Direction:"+repr(self)

    def __repr__(self) -> str:
        return str(self.current)

if(__name__=="__main__"):
    x=Compass()
    print(x.direction())
    x.rotate(2)
    print(x.direction())
    x.rotate(-4)
    print(x.direction())
    x.rotate(-3)
    print(x.direction())