from genome import Gene
# from neurons import SensorNeuron,ActionNeuron,InnerNeuron
from weight import Weight
class Connection():
    MAX16BITINT=(1<<16)
    '''Connection is a link information , contains source details ,destination details ,and weight details '''
    def __init__(self ,gene:Gene=None,source_id:int=None,source_add:int=None,dest_id:int=None,dest_add:int=None,weight:Weight=None) -> None:
        if(gene==None):
            self.source_id=source_id
            self.source_add=source_add
            self.dest_id=dest_id
            self.dest_add=dest_add
            self.weight=weight
            self.gene:Gene=self.generateGene()
        else:
            self.gene=gene
            self.source_id=int(gene.bin[0])
            self.source_add=int(gene.bin[1:8],2)#%SensorNeuron.SIZE if self.source_id==0 else int(gene.bin[1:8],2)%InnerNeuron.SIZE
            self.dest_id=int(gene.bin[8])
            self.dest_add=int(gene.bin[9:16],2)#%InnerNeuron.SIZE if self.dest_id==0 else int(gene.bin[9:16],2)%ActionNeuron.SIZE 
            self.weight=Weight(Connection.signed16bitB2D(gene.bin[16:]))

        # print(self.source_id,int(self.source_add,2),self.dest_id,int(self.dest_add,2),Connection.signed16bitB2D(self.weight))
        self.array=(self.source_id,self.source_add,self.dest_id,self.dest_add,self.weight)
      
    def signed16bitB2D(value:str)->int:
        '''Converts binary 16 bit number to signed 16 bit decimal'''
        if(len(value)!=16):
            raise Exception("Invalid Binary Conversion")
        if(value[0]=='1'):
            return int(value,2)-Connection.MAX16BITINT
        return int(value,2)

    def signed16bitD2B(value:int)->str:
        '''Converts 16 bit signed Integer to 16 bit binary number'''
        if(value<-Connection.MAX16BITINT/2 or value>=int(Connection.MAX16BITINT/2)):
            raise Exception("Invalid Decimal Conversion to bin")
        
        if(value>0):
            return '{0:016b}'.format(value,'b')
        return '{0:016b}'.format(value+Connection.MAX16BITINT,'b')
    
    def update(self,__o:object)->None:
        self.source_add=__o.source_add
        self.source_id=__o.source_id
        self.dest_add=__o.dest_add
        self.dest_id=__o.dest_id
        self.weight=__o.weight

    def generateGene(self)->Gene:
        result=str(self.source_id)
        result+=format(self.source_add,'07b')
        result+=str(self.dest_id)
        result+=format(self.source_add,'07b')
        result+=Connection.signed16bitD2B(self.weight.getOriginalValue())
        # print(result)
        return Gene(bin=result)
        

    def __eq__(self, __o: object) -> bool:
        return self.source_add==__o.source_add and self.source_id==__o.source_id and self.dest_add==__o.dest_add and self.dest_id==__o.dest_id
        
    def __str__(self) -> str:
        return "Connection : "+" ".join(str(i) for i in [self.source_id,self.source_add,self.dest_id,self.dest_add,self.weight])

    def __repr__(self) -> str:
        return "Connection : "+" ".join(str(i) for i in [self.source_id,self.source_add,self.dest_id,self.dest_add,self.weight])

class ConnectionArray():
    def __init__(self,linkArray:list[Connection])->None:
        self.links=linkArray

    def find(self,__link:Connection)->Connection:
        for i in self.links:
            if(i==__link):
                return i
        raise Exception("No Connection Found")

    def update(self,oldlink,newlink)->None:
        tmp=self.find(oldlink)
        tmp.update(newlink)

    def removeConnection(self,__o:object)->None:
        self.links.remove(self.find(__o))
    
    def __str__(self) -> str:
        return "ConnectionArray : "+str(self.links)

    def __getitem__(self,index:int)->Connection:
        return self.links[index]
    
    def __len__(self)->int:
        return len(self.links)

if __name__=="__main__":
    a=ConnectionArray([Connection(Gene()) for i in range(10)])
    print(a)
    # a.update(a[0],a[4])
    a.removeConnection(a[0])
    print(a)
    # for i in a:
    #     print(i)
    # print(Connection.signed16bitD2B(32767))
