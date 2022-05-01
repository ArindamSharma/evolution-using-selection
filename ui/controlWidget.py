import tkinter as tk

# import sys
# sys.path.append('../src')

# from creature import Creature
# from genome import Genome

from color import Color

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
		self.button2=tk.Button(self,text="Pause")
		self.button2.pack()
		self.button2=tk.Button(self,text="Save")
		self.button2.pack()
		self.button1=tk.Button(self,text="feature1")
		self.button1.pack()
		self.button2=tk.Button(self,text="feature2")
		self.button2.pack()
		self.button2=tk.Button(self,text="freature3")
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

