from creature import Creature
from evolution import Evolution
class Selection():
    def __init__(self) -> None:
        pass
    
    def selectionCriteria1(self,creature:Creature)->bool:
        '''this is custom function thats changes with different criteria'''
        return True
        if(creature.location[0]>self.world_size/2):
            return True
        return False

    def selectionCriteria2(self,creature:Creature)->bool:
        '''this is custom function thats changes with different criteria'''
        return True
        if(creature.location[1]>self.world_size/2):
            return True
        return False