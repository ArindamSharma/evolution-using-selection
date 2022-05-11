from ast import arg
from time import sleep
import tkinter as tk

import sys


sys.path.append('../src')

from evolution import Evolution
from creature import Creature
from genome import Genome

from locWidget import LocWidget
from controlWidget import StatusWidget
from graphWidget import GraphWidget
from color import Color
import threading

class Simulator(tk.Tk):

	def __init__(self,*arg,**kwarg):
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
		for F in (MainPage,EvolutionSimPage,ConfigPage,GenomeSimPage,SettingPage,ThemePage):
			self.frames[F]=F(container,self)
			self.frames[F].grid(row=0,column=0,sticky=tk.NSEW)
			# print(self.frames[F])

		self.show_frame(MainPage)
		# self.show_frame(EvolutionSimPage)
		
		# self.protocol("WM_DELETE_WINDOW", self.window_exit)
	
	def show_frame(self,widget):
		self.frames[widget].tkraise()
	
	# def window_exit(self):
	# 	pass

class MainPage(tk.Frame):
	
	def buttonpress1(self):
		self.controllerFrame.show_frame(EvolutionSimPage)
	def buttonpress2(self):
		print("No Function Assigned Yet")
		# self.controllerFrame.show_frame(EvolutionSimPage)
	def buttonpress3(self):
		self.controllerFrame.show_frame(GenomeSimPage)
	def buttonpress4(self):
		self.controllerFrame.show_frame(SettingPage)
	def buttonpress5(self):
		print("Thankyou for Using Simulator")
		self.controllerFrame.destroy()

	def __init__(self,parent,controllerFrame,*arg,**kwarg):
		tk.Frame.__init__(self,parent,*arg,**kwarg,bg=Color.rgbToHex(0,90,109))
		self.configure(padx=10,pady=10)
		self.controllerFrame=controllerFrame

		self.labelFrame=tk.Frame(self,bg=Color.rgbToHex(0,90,109))
		self.labelFrame.pack(pady=50)
		self.label1=tk.Label(self.labelFrame,text="Visualization Tool",bg=Color.rgbToHex(0,90,109),fg=Color.white,font=("Arial", 55))
		self.label1.pack()
		self.label2=tk.Label(self.labelFrame,text="For Genetic Algorithm",bg=Color.rgbToHex(0,90,109),fg=Color.white,font=("Arial", 25))
		self.label2.pack()

		self.button1=tk.Button(self,text="Evolution Simluator",command=self.buttonpress1)
		self.button1.pack()
		self.button2=tk.Button(self,text="Load Simluator",command=self.buttonpress2)
		self.button2.pack()
		self.button3=tk.Button(self,text="Genome Simluator",command=self.buttonpress3)
		self.button3.pack()
		self.button4=tk.Button(self,text="Setting",command=self.buttonpress4)
		self.button4.pack()
		self.button5=tk.Button(self,text="Exit",command=self.buttonpress5)
		self.button5.pack(side=tk.BOTTOM,pady=20)
		for button in [self.button5,self.button4,self.button3,self.button2,self.button1]:
			button.config(bg=Color.rgbToHex(1,45,54),padx=40,pady=10,font=("Arial", 15),fg=Color.white)
			button.pack(pady=10)

class BasePageTemplate(tk.Frame):
	def __init__(self,parent:tk.Frame,controllerFrame:tk.Tk,title,backcommand,*arg,**kwarg):
		tk.Frame.__init__(self,parent,*arg,**kwarg,bg=Color.light_gray)
		self.controllerFrame=controllerFrame
		
		self.rootFrame=tk.Frame(self)
		self.rootFrame.pack(fill=tk.BOTH,expand=True)
		
		self.statusBar=tk.Frame(self.rootFrame,bg=Color.rgbToHex(0,90,109))
		self.statusBar.pack(side=tk.TOP,fill=tk.X)
		self.backbutton=tk.Button(self.statusBar,text="Back",padx=10,command=backcommand,bg=Color.rgbToHex(1,45,54),font=("Arial", 10),fg=Color.white)
		self.backbutton.pack(side=tk.LEFT)
		
		self.pageLabel=tk.Label(self.statusBar,text=title,bg=Color.rgbToHex(0,90,109),fg=Color.white)
		self.pageLabel.pack(side=tk.RIGHT,fill=tk.X,expand=True)

		self.mainFrame=tk.Frame(self.rootFrame)
		self.mainFrame.pack(side=tk.BOTTOM,fill=tk.BOTH,expand=True)

class EvolutionSimPage(BasePageTemplate,Evolution):
	def backbutton(self):
		self.controllerFrame.show_frame(MainPage)
		
	def configbutton(self):
		self.controllerFrame.show_frame(ConfigPage)

	def feedForwardThread(self):
		self.feedthread=threading.Thread(target=self.FeedForward)
		self.feedthread.start()

	def FeedForward(self):
		tmp_flag=0
		print("Thread Started")
		
		population=None
		if(StatusWidget.initialize==False):
			population=[Genome(size=self.genome_size) for i in range(self.population_size)]
		
		for gen in range(self.max_generation):
			# print(gen)
			
			self.graphFrame.locGraph.clearPoints()
			self.refreshLocation()
			self.introducingPopulation(population)
			self.graphFrame.locGraph.initPoints()
			for steps in range(self.step_per_gen):
				# print(steps)
				# one day of creature life
				for creature in Creature.envLoc:
					creature.grow()
				# print("Day",steps,"completed")
				# map updation
				self.graphFrame.locGraph.clearPoints()
				self.graphFrame.locGraph.initPoints()
				# self.graphFrame.locGraph.update()
				# print("Cleared map")
				# sleep(0.05)
				self.statusBox.parameter_current_gen.text.set(str(gen+1))
				self.statusBox.parameter_day_count.text.set(str(steps+1))
				# print("updated status",self.statusBox.button_play_pause.toggle_flag)
				if(self.statusBox.button_play_pause.toggle_flag==True):
					tmp_flag=1
					return
				# print("not paused")
			if(tmp_flag==1):
				return
			# after generation is over 
			self.terminateUnfit(SelectionCriteria=self.selectionCriteria2)
			population=self.repopulate([i.getGenome() for i in Creature.envLoc])
            

	def __init__(self,parent:tk.Frame,controllerFrame:tk.Tk,*arg,**kwarg):
		BasePageTemplate.__init__(self,parent,controllerFrame,"Evolution Simulator",self.backbutton,*arg,**kwarg)
		self.configure(padx=10,pady=10)
		self.controllerFrame=controllerFrame

		Evolution.__init__(self)
		# Upper World Frame
		self.graphStatusFrame=tk.Frame(self.mainFrame,bg=Color.dark_gray)
		self.graphStatusFrame.pack(side=tk.TOP,fill=tk.X)

		# World
		self.graphFrame=LocWidget(self.graphStatusFrame,Creature.envLoc,height=500,width=500,mat_size=self.world_size,title="World Map")
		self.graphFrame.pack(side=tk.RIGHT)
		# Status
		self.statusBox=StatusWidget(self.graphStatusFrame,self,bg=Color.rgbToHex(0,90,109))
		self.statusBox.pack(side=tk.LEFT,expand=True,fill=tk.BOTH)

		# Graph
		self.genGraph=GraphWidget(self.mainFrame,bg=Color.aqua)
		self.genGraph.pack(side=tk.BOTTOM,fill=tk.BOTH,expand=True)

class ConfigPage(BasePageTemplate,tk.Frame):
	def backbutton(self):
		self.controllerFrame.show_frame(EvolutionSimPage)

	def __init__(self,parent,controllerFrame,*arg,**kwarg):
		tk.Frame.__init__(self,parent,*arg,**kwarg,bg="light pink")
		BasePageTemplate.__init__(self,parent,controllerFrame,"Configure Simulator Parameters",self.backbutton,*arg,**kwarg)
		self.configure(padx=10,pady=10)

class GenomeSimPage(BasePageTemplate,tk.Frame):
	def backbutton(self):
		self.controllerFrame.show_frame(MainPage)

	def __init__(self,parent,controllerFrame,*arg,**kwarg):
		tk.Frame.__init__(self,parent,*arg,**kwarg,bg="light pink")
		BasePageTemplate.__init__(self,parent,controllerFrame,"Genome Simulator",self.backbutton,*arg,**kwarg)
		self.configure(padx=10,pady=10)

class SettingPage(BasePageTemplate,tk.Frame):
	def backbutton(self):
		self.controllerFrame.show_frame(MainPage)

	def __init__(self,parent,controllerFrame,*arg,**kwarg):
		tk.Frame.__init__(self,parent,*arg,**kwarg,bg="light pink")
		BasePageTemplate.__init__(self,parent,controllerFrame,"Setting",self.backbutton,*arg,**kwarg)
		self.configure(padx=10,pady=10)


class ThemePage(BasePageTemplate,tk.Frame):
	def backbutton(self):
		self.controllerFrame.show_frame(MainPage)

	def __init__(self,parent,controllerFrame,*arg,**kwarg):
		tk.Frame.__init__(self,parent,*arg,**kwarg,bg="light pink")
		BasePageTemplate.__init__(self,parent,controllerFrame,"Theme Configuration",self.backbutton,*arg,**kwarg)
		self.configure(padx=10,pady=10)


if(__name__=="__main__"):	
	app=Simulator()
	
	app.mainloop()