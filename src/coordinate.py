class Coordinate():
    '''Object Stores 
    
    x coordinate 
    
    y coordinate'''
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __eq__(self, __o: object) -> bool:
        return self.x==__o.x and self.y==__o.y
        
    def __cmp__(self, __o: object) -> bool:
        return self.x==__o.x and self.y==__o.y
        
    def __add__(self,__o:object):
        __o.x+=self.x
        __o.y+=self.y
        return __o

    def __hash__(self) -> int:
        return hash(str(self.x)+str(self.y))

    def __repr__(self) -> str:
        return "Coordinate "+str(self.x)+","+str(self.y) 
        
class people():
    def __init__(self,p1,p2,p3):
        self.param1=p1
        self.param2=p2
        self.param3=p3
    def __repr__(self) -> str:
        return "People "+",".join(str(i) for i in [self.param1,self.param2,self.param3])
if(__name__=="__main__"):
    from random import randint
    d:dict[Coordinate,people]={}
    for i in range(5):
        for j in range(5):
            d[Coordinate(i,j)]=people(randint(0,7),randint(0,7),randint(0,7))
    
    print(d)
    for i in d:
        i.x=100
        i.y=100
        break
    # print(d[Coordinate(0,0)])
    print(d)
    print(Coordinate(0,0)+Coordinate(0,-1))
    print(d[Coordinate(0,0)])
    # print("--------")
    # a=[]
    # for i in range(5):
    #     for j in range(5):
    #         a.append(Coordinate(i,j))
    # print(a)
    # print(a.remove(Coordinate(0,0)))
    # print(a)
