import random
import tkinter as tk

import sys
from cv2 import exp

from numpy import size
sys.path.append('../src')

from evolution import Evolution
from ui_locCanvas import LocCanvas
from color import Color
from random import choice
from creature import Creature
from genome import Genome

class Simulator(tk.Tk,Evolution):

	def __init__(self,*arg,**kwarg):
		Evolution.__init__(self,)
		tk.Tk.__init__(self,*arg,**kwarg)
		self.title("Evolution Using Natural Selection (GA)")
		self.geometry("900x800+100+100")
		# self.eval('tk::PlaceWindow . center')
		# self.minsize(500,300)
		self.resizable(0,0)
		
		container=tk.Frame(self,bg="light green")
		container.pack(side=tk.TOP,fill=tk.BOTH,expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)
		# container.configure(padx=10,pady=10)
		
		# self.iconphoto(False,tk.PhotoImage(""))

		self.frames={}
		for F in (HomePage,ExitPage):
			self.frames[F]=F(container,self)
			self.frames[F].grid(row=0,column=0,sticky=tk.NSEW)
			# print(self.frames[F])

		# self.show_frame(ExitPage)
		self.show_frame(HomePage)
	
	def show_frame(self,widget):
		self.frames[widget].tkraise()

class HomePage(tk.Frame):

	def __init__(self,parent:tk.Frame,controllerFrame:tk.Tk,*arg,**kwarg):
		tk.Frame.__init__(self,parent,*arg,**kwarg,bg=Color.light_gray)
		self.configure(padx=10,pady=10)

		# Upper World Frame
		graphStatusFrame=tk.Frame(self,bg=Color.alice_blue)
		graphStatusFrame.pack(side=tk.TOP,fill=tk.X)
		# World
		graphFrame=WorldWidget(graphStatusFrame,height=500,width=500,background=Color.light_grey)
		graphFrame.pack(side=tk.LEFT)
		# Status
		statusBox=StatusWidget(graphStatusFrame,bg=Color.light_green)
		statusBox.pack(side=tk.RIGHT,expand=True,fill=tk.BOTH)

		# Graph
		genGraph=GraphWidget(self,bg=Color.aqua)
		genGraph.pack(side=tk.BOTTOM,fill=tk.BOTH,expand=True)


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



class WorldWidget(tk.Frame):
	def __init__(self,parent,height,width,*arg,**kwarg):
		tk.Frame.__init__(self,parent,*arg,**kwarg)
		
		self.label=tk.Label(self,text="Gen 0")
		self.label.pack(side=tk.TOP,fill=tk.X)

		self.mat_size=128
		self.locGraph=LocCanvas(self,height,width,bg=Color.white,mat_size=self.mat_size,dot_size=4)
		self.locGraph.pack(padx=10,pady=10)
		pp={}
		for i in range(self.mat_size):
			for j in range(self.mat_size):
				if(choice([1]+1*[0,0,0,0,0,0,0,0,0,0,0,0,0])):
					loc=(i,j)
					pp[loc]=Creature(Genome(size=4),loc)

		self.locGraph.initPoints(pp)

class StatusWidget(tk.Frame):
	def __init__(self,parent,*arg,**kwarg):
		tk.Frame.__init__(self,parent,*arg,**kwarg)
		
		self.label=tk.Label(self,text="Parameters ")
		self.label.pack(side=tk.TOP,fill=tk.X)

		self.parameterFrame=tk.Frame(self,)
		self.parameterFrame.pack(fill=tk.X)

		parameter3=parameter(self.parameterFrame,text="Current Generation",default_value=0)
		parameter3.pack(fill=tk.X)
		parameter1=parameter(self.parameterFrame,text="World Size",default_value=128)
		parameter1.pack(fill=tk.X)

		parameter2=parameter(self.parameterFrame,text="Population",default_value=1000)
		parameter2.pack(fill=tk.X)

		parameter3=parameter(self.parameterFrame,text="Steps Per Generation",default_value=300)
		parameter3.pack(fill=tk.X)

		parameter3=parameter(self.parameterFrame,text="Genome Size",default_value=4)
		parameter3.pack(fill=tk.X)
		
		parameter3=parameter(self.parameterFrame,text="Mutation Rate",default_value=0.01)
		parameter3.pack(fill=tk.X)

		self.button1=tk.Button(self,text="Play")
		self.button1.pack()
		self.button2=tk.Button(self,text="Puase")
		self.button2.pack()
		self.button2=tk.Button(self,text="Save")
		self.button2.pack()

class parameter(tk.Frame):
	def __init__(self,parent,*arg,**kwarg):
		tk.Frame.__init__(self,parent,*arg)

		self.config(padx=10)
		self.label=tk.Label(self,text=kwarg["text"],anchor=tk.W)
		self.label.pack(side=tk.LEFT,fill=tk.X,expand=True)

		self.userinput=tk.Entry(self,width=10)
		self.userinput.pack(side=tk.RIGHT)
		self.userinput.insert(0,kwarg["default_value"])


class ExitPage(tk.Frame):

	def __init__(self,parent,controllerFrame,*arg,**kwarg):
		tk.Frame.__init__(self,parent,*arg,**kwarg,bg="light pink")
		self.configure(padx=10,pady=10)


if(__name__=="__main__"):	
	app=Simulator()
	app.mainloop()