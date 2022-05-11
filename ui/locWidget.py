import tkinter as tk

import sys
sys.path.append('../src')


from color import Color
from random import choice,randint
from time import sleep

class LocCanvas(tk.Canvas):

    pointArray={}
    def __init__(self,parent:tk.Frame,height,width,mat_size,dot_size,*arg,**kwarg):
        tk.Canvas.__init__(self,parent,*arg,**kwarg,height=height,width=width,highlightthickness=0)
        self.parent=parent
        self.dot_size=dot_size
        self.mat_size=mat_size
        self.height=height
        self.width=width
        self.grid_space_v=(height-(mat_size*dot_size))/(mat_size-1)
        self.grid_space_h=(width-(mat_size*dot_size))/(mat_size-1)
        # print(self.grid_space_v)
        self.bind("<Button-1>", self.button1)

    def initPoints(self,):
        # for i in range(self.mat_size):
        #     for j in range(self.mat_size):
        #         self.addPoint(i,j,'red')

        # print(*[(i.id,i.location,i.direction) for i in self.parent.env],sep="\n")

        for creature in self.parent.env:
            self.addPoint(creature.location.x,creature.location.y,Color.rgbToHex(creature.r,creature.g,creature.b))

        self.update()

    def clearPoints(self)->None:
        # for i in LocCanvas.pointArray:
        #     self.delete(LocCanvas.pointArray[i])
        LocCanvas.pointArray.clear()
        self.delete(tk.ALL)

    def addPoint(self,x:float,y:float,color:str):
        # print(x,y)
        tmploc=(x,y)
        x*=self.grid_space_h+self.dot_size
        y*=self.grid_space_v+self.dot_size
        # print(tmploc)
        # print(x,y,x+self.dot_size,y+self.dot_size)
        LocCanvas.pointArray[tmploc]=self.create_oval(x,y,x+self.dot_size,y+self.dot_size,fill=color,outline='')
        
    def button1(self,event):
        for _ in range(50+1):
            print("Day",_,end="\r")
            self.clearPoints()
            
            
            for creature in self.parent.env:
                creature.grow()
            self.initPoints()
            break
            # self.parent.label.config(text="Gen "+str(_))
            # sleep(0.05)

class LocWidget(tk.Frame):
    def __init__(self,parent:tk.Widget,envLoc:list,height,width,mat_size:int,title:str="",*arg,**kwarg):
        tk.Frame.__init__(self,parent,*arg,**kwarg)
        self.env=envLoc
        self.label=tk.Label(self,text=title)
        self.label.pack(side=tk.TOP,fill=tk.X)

        # self.env=None
        self.locGraph=LocCanvas(self,height,width,bg=Color.white,mat_size=mat_size,dot_size=5)
        self.locGraph.pack()
        # self.locGraph.initPoints()


if(__name__=="__main__"):
    
    from creature import Creature
    from coordinate import Coordinate
    from genome import Genome
    from evolution import Evolution
    root=tk.Tk()
    root.title("Testing LocCanvas")
    root.geometry("650x650")
    root.configure(bg="light grey")
    mat_size=128

    a=Evolution()

    graphFrame=LocWidget(root,Creature.envLoc,height=600,width=600,mat_size=mat_size,title="World Simulator")
    graphFrame.pack(expand=True)
    a.introducingPopulation()
    # print(len(pp),mat_size**2)
    root.mainloop()