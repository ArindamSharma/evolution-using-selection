from creature import Creature
class Selection():
    '''All custom defined selection criteria must return bool value '''
    def __inti__(self):
        pass
    
    def selectionCriteria1(self,creature:Creature)->bool:
        '''this is custom function thats changes with different criteria'''
        if(creature.location[0]>self.world_size/2):
            return True
        return False

    def selectionCriteria2(self,creature:Creature)->bool:
        '''this is custom function thats changes with different criteria'''
        if(creature.location[1]>self.world_size/2):
            return True
        return False