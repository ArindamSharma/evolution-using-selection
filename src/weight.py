class Weight():
    CONSTANT=(1<<15)/4
    '''weight should be in range of -4.0 - 4.0'''
    def __init__(self,value:int):
        self.value=value/Weight.CONSTANT

    def getOriginalValue(self)->int:
        return int(self.value*Weight.CONSTANT)
    
    def __eq__(self, __o: object) -> bool:
        self.weight=__o.weight

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return str(self.value)
