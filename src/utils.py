class Pair():
    '''Pair equvalent to c++ 17 Pair in STL '''
    def __init__(self,first,second) -> None:
        self.first=first
        self.second=second
    
    def __str__(self) -> str:
        return "Pair ["+str(self.first)+","+str(self.second)+"]"

    def __repr__(self) -> str:
        return "["+str(self.first)+","+str(self.second)+"]"


if(__name__=="__main__"):
    p=[1,2,3,4,5,6]
    x=[]
    # x:list[Pair]=[Pair(i,j) for i,j in zip(range(10),range(10))]
    # for i in p:
    #     x.append(i)

    # for i in p:
    #     x.append(i)
    x=[i for i in p]
    print(id(x))
    p[0]=5
    print(id(p))
    # y:list[Pair]=[]
    # for i in x:
    #     y.append(Pair(i,0))
    
    print(x)

    # y[3].second=9
    print(x)