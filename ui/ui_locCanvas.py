import tkinter as tk
from creature import Creature
from genome import Genome

class LocCanvas(tk.Canvas):

    def __init__(self,parent,height,width,dot_size,*arg,**kwarg):
        tk.Canvas.__init__(self,parent,*arg,**kwarg,height=height,width=width,highlightthickness=0)
        self.dot_size=dot_size

    def initPoints(self,matrix:list[Creature]):
        pass 


if(__name__=="__main__"):
    root=tk.Tk()
    root.title("Testing LocCanvas")
    root.geometry("650x650")
    root.configure(bg="grey")
    graph=LocCanvas(root,600,600,bg="green",dot_size=3)

    graph.pack()
    pp=[]
    # for i in range(100):
    #     pp.append(Creature(Genome(size=4),))
    root.mainloop()