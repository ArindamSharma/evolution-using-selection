import tkinter as tk

import sys
sys.path.append('../src')

from creature import Creature
from color import Color
from genome import Genome
from random import choice
from time import sleep


class LocCanvas(tk.Canvas):

    def __init__(self,parent,height,width,mat_size,dot_size,*arg,**kwarg):
        tk.Canvas.__init__(self,parent,*arg,**kwarg,height=height,width=width,highlightthickness=0)
        self.dot_size=dot_size
        self.mat_size=mat_size
        self.height=height
        self.width=width
        self.grid_space_v=(height-(mat_size*dot_size))/(mat_size-1)
        self.grid_space_h=(width-(mat_size*dot_size))/(mat_size-1)
        self.pointArray={}
        # print(self.grid_space_v)
        self.bind("<Button-1>", self.button1)

    def initPoints(self,loc:dict[tuple,any]):
        # print(loc)
        
        # for i in range(self.mat_size):
        #     for j in range(self.mat_size):
        #         self.addPoint(i,j,'red')
        for i in loc:
            self.addPoint(i[0],i[1],Color.rgbToHex(255,0,0))

    def clearPoints(self)->None:
        for i in self.pointArray:
            self.delete(self.pointArray[i])
        self.pointArray.clear()

    def addPoint(self,x:float,y:float,color:str):
        # print(x,y)
        tmploc=(x,y)
        x*=self.grid_space_h+self.dot_size
        y*=self.grid_space_v+self.dot_size
        # print(tmploc)
        # print(x,y,x+self.dot_size,y+self.dot_size)
        self.pointArray[tmploc]=self.create_oval(x,y,x+self.dot_size,y+self.dot_size,fill=color,outline='')
        
    def button1(self,event):
        for _ in range(20+1):
            print("Day",_,end="\r")
            self.clearPoints()
            pp={}
            for i in range(self.mat_size):
                for j in range(self.mat_size):
                    if(choice([1]+1*[0,0,0,0,0,0,0,0,0,0,0,0,0])):
                        loc=(i,j)
                        pp[loc]=Creature(Genome(size=4),loc)
            
            self.initPoints(pp)
            self.update()
            sleep(0.1)



if(__name__=="__main__"):
    root=tk.Tk()
    root.title("Testing LocCanvas")
    root.geometry("650x650")
    root.configure(bg="light grey")
    mat_size=100
    graph=LocCanvas(root,600,600,bg=Color.light_blue,mat_size=mat_size,dot_size=6)
    graph.pack(expand=True)
    pp={}
    for i in range(mat_size):
        for j in range(mat_size):
            if(choice([1]+1*[0,0,0,0,0,0,0,0,0,0,0,0,0])):
                loc=(i,j)
                pp[loc]=Creature(Genome(size=4),loc)
    
    graph.initPoints(pp)

    # print(len(pp),mat_size**2)
    root.mainloop()