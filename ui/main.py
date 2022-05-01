import tkinter as tk

import sys
sys.path.append('../src')

from evolution import Evolution
# from creature import Creature
# from genome import Genome

from locWidget import LocWidget
from controlWidget import StatusWidget
from graphWidget import GraphWidget
from color import Color

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
		graphStatusFrame=tk.Frame(self,bg=Color.dark_gray)
		graphStatusFrame.pack(side=tk.TOP,fill=tk.X)
		# World
		graphFrame=LocWidget(graphStatusFrame,height=500,width=500)
		graphFrame.pack(side=tk.LEFT)
		# Status
		statusBox=StatusWidget(graphStatusFrame,bg=Color.light_green)
		statusBox.pack(side=tk.RIGHT,expand=True,fill=tk.BOTH)

		# Graph
		genGraph=GraphWidget(self,bg=Color.aqua)
		genGraph.pack(side=tk.BOTTOM,fill=tk.BOTH,expand=True)


class ExitPage(tk.Frame):

	def __init__(self,parent,controllerFrame,*arg,**kwarg):
		tk.Frame.__init__(self,parent,*arg,**kwarg,bg="light pink")
		self.configure(padx=10,pady=10)


if(__name__=="__main__"):	
	app=Simulator()
	app.mainloop()