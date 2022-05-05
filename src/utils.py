class Pair():
    '''Pair equvalent to c++ 17 Pair in STL '''
    def __init__(self,first,second) -> None:
        self.first=first
        self.second=second
    
    def __str__(self) -> str:
        return "Pair ["+self.first+","+self.second+"]"

    def __repr__(self) -> str:
        return "["+str(self.first)+","+str(self.second)+"]"