import tkinter as tk

# import sys
# sys.path.append('../src')

# from creature import Creature
# from genome import Genome

from color import Color

class GraphWidget(tk.Frame):
	def __init__(self,parent,*arg,**kwarg):
		tk.Frame.__init__(self,parent,*arg,**kwarg)
		
		self.buttonFrame=tk.Frame(self)
		self.buttonFrame.pack()

		self.button1=tk.Button(self.buttonFrame,text="All")
		self.button1.pack()
		self.button2=tk.Button(self.buttonFrame,text="Gen Vs Diversity")
		self.button2.pack()

		self.graph1=SingleGraphWidget(self,bg=Color.green)
		# self.graph1.grid(row=0,column=0,sticky=tk.NSEW)
		self.graph1.pack()

        
class SingleGraphWidget(tk.Frame):
	def __init__(self,parent,*arg,**kwarg):
		tk.Frame.__init__(self,parent,*arg,**kwarg)


if(__name__=="__main__"):
    root=tk.Tk()
    root.title("Testing LocCanvas")
    root.geometry("650x650")
    root.configure(bg="light grey")
	
    graphFrame=GraphWidget(root,bg=Color.light_coral)
    graphFrame.pack(expand=True,fill=tk.BOTH)

    # print(len(pp),mat_size**2)
    root.mainloop()