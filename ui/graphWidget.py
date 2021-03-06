import tkinter as tk

# import sys
# sys.path.append('../src')

# from creature import Creature
# from genome import Genome

from color import Color

class GraphWidget(tk.Frame):
	def allgraph(self):
		self.button_all.config(bg=Color.rgbToHex(1,45,54),fg=Color.white)
		self.button_survival.config(bg=Color.white_smoke,fg=Color.black)
		self.button_diversity.config(bg=Color.white_smoke,fg=Color.black)
		self.graph.show_frame(AllGraph)
	
	def diversity(self):
		self.button_diversity.config(bg=Color.rgbToHex(1,45,54),fg=Color.white)
		self.button_all.config(bg=Color.white_smoke,fg=Color.black)
		self.button_survival.config(bg=Color.white_smoke,fg=Color.black)
		self.graph.show_frame(Diversity)

	def survival(self):
		self.button_survival.config(bg=Color.rgbToHex(1,45,54),fg=Color.white)
		self.button_all.config(bg=Color.white_smoke,fg=Color.black)
		self.button_diversity.config(bg=Color.white_smoke,fg=Color.black)
		self.graph.show_frame(Survival)
	
	def __init__(self,parent,simparam,*arg,**kwarg):
		tk.Frame.__init__(self,parent,*arg,**kwarg)
		
		self.buttonFrame=tk.Frame(self)
		self.buttonFrame.pack(side=tk.TOP,fill=tk.X)

		self.button_all=tk.Button(self.buttonFrame,text="Gen Vs All",command=self.allgraph)
		self.button_all.pack(side=tk.LEFT)
		self.button_diversity=tk.Button(self.buttonFrame,text="Gen Vs Diversity",command=self.diversity)
		self.button_diversity.pack(side=tk.LEFT)
		self.button_survival=tk.Button(self.buttonFrame,text="Gen Vs Survival",command=self.survival)
		self.button_survival.pack(side=tk.LEFT)

		self.graph=SingleGraphWidget(self,simparam)
		self.graph.pack(fill=tk.BOTH,expand=True)

        
class SingleGraphWidget(tk.Frame):
	def __init__(self,parent,simparam,*arg,**kwarg):
		tk.Frame.__init__(self,parent,*arg,**kwarg)
		
		container=tk.Frame(self,bg="light green")
		container.pack(side=tk.TOP,fill=tk.BOTH,expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)
		self.frames={}

		for F in (NoPage,AllGraph,Diversity,Survival):
			self.frames[F]=F(container,self,simparam)
			self.frames[F].grid(row=0,column=0,sticky=tk.NSEW)
			# print(self.frames[F])

		self.show_frame(NoPage)
	
	def show_frame(self,widget):
		self.frames[widget].tkraise()
	
class AllGraph(tk.Frame):
	
	pointsArray={}
	def __init__(self,parent:tk.Frame,controllerFrame:tk.Tk,simparam,*arg,**kwarg):
		tk.Frame.__init__(self,parent,*arg,**kwarg,bg=Color.light_coral)
		self.controllerFrame=controllerFrame
		self.main=tk.Canvas(self,bg=Color.light_coral)
		self.main.pack(fill=tk.BOTH,expand=True)
		self.main.create_text(10,100,text="Survivals",angle=90)
		self.main.create_text(200,190,text="Generations")

	def addPoints(self,x,y):
		pass

	def clearPoints(self):
		pass

class Diversity(tk.Frame):

	pointsArray={}
	def __init__(self,parent:tk.Frame,controllerFrame:tk.Tk,simparam,*arg,**kwarg):
		tk.Frame.__init__(self,parent,*arg,**kwarg,bg=Color.light_green)
		self.controllerFrame=controllerFrame
		self.main=tk.Canvas(self,bg=Color.light_green)
		self.main.pack(fill=tk.BOTH,expand=True)
		self.main.create_text(10,100,text="Survivals",angle=90)
		self.main.create_text(200,190,text="Generations")

	def addPoints(self,x,y):
		pass

	def clearPoints(self):
		pass

class Survival(tk.Frame):
	pointsArray={}
	def __init__(self,parent:tk.Frame,controllerFrame:tk.Tk,simparam,*arg,**kwarg):
		tk.Frame.__init__(self,parent,*arg,**kwarg,bg=Color.light_grey)
		self.controllerFrame=controllerFrame
		self.main=tk.Canvas(self,bg=Color.light_grey)
		self.main.pack(fill=tk.BOTH,expand=True)
		# print(self.main.winfo_height(),self.main.winfo_width())
		self.main.create_text(10,100,text="Survivals",angle=90)
		self.main.create_text(200,190,text="Generations")

	def addPoints(self,x,y):
		pass

	def clearPoints(self):
		pass
	
class NoPage(tk.Frame):

	def __init__(self,parent:tk.Frame,controllerFrame:tk.Tk,simparam,*arg,**kwarg):
		tk.Frame.__init__(self,parent,*arg,**kwarg,bg=Color.light_blue)
		# self.controllerFrame=controllerFrame

		self.label=tk.Label(self,text="Please Select Graph From Above Row",bg=Color.light_slate_gray)
		self.label.pack(fill=tk.BOTH,expand=True)

if(__name__=="__main__"):
    root=tk.Tk()
    root.title("Testing LocCanvas")
    root.geometry("650x650")
    root.configure(bg="light grey")
	
    graphFrame=GraphWidget(root,bg=Color.light_coral)
    graphFrame.pack(expand=True,fill=tk.BOTH)

    # print(len(pp),mat_size**2)
    root.mainloop()