import tkinter as tk

# import sys
# sys.path.append('../src')

# from creature import Creature
# from genome import Genome

from color import Color
from buttonWidget import ToggleButtonWidget
# from creature import Creature
# from locWidget import LocCanvas

# from main import ConfigPage 

class StatusWidget(tk.Frame):
	initialize=False
	def updateEvoParamFromController(self):
		self.evoFrame.max_generation=int(self.parameter_max_gen.userinput.get())
		self.evoFrame.world_size=int(self.parameter_world_size.userinput.get())
		self.evoFrame.population_size=int(self.parameter_population_size.userinput.get())
		self.evoFrame.step_per_gen=int(self.parameter_steps_per_gen.userinput.get())
		self.evoFrame.genome_size=int(self.parameter_genome_size.userinput.get())
		self.evoFrame.mutation_rate=float(self.parameter_mutation_rate.userinput.get())
		self.evoFrame.inner_neuron=int(self.parameter_inner_neuron.userinput.get())


	def applybutton(self):
		StatusWidget.initialize=True
		self.evoFrame.graphFrame.locGraph.clearPoints()
		self.evoFrame.refreshLocation()
		# print(len(Creature.envLoc))
		self.updateEvoParamFromController()
		self.evoFrame.introducingPopulation()
		self.evoFrame.graphFrame.locGraph.initPoints()
		# self.evoFrame.graphFrame.locGraph.update()

	def clearMap(self):
		self.evoFrame.refreshLocation()
		self.evoFrame.graphFrame.locGraph.clearPoints()
		StatusWidget.initialize=False
		
		# self.evoFrame.graphFrame.locGraph.update()
		# print(len(Creature.envLoc))
		# print(len(LocCanvas.pointArray))

	def playpause(self):
		if(self.button_play_pause.toggle_flag):
			print("Play")
			
			for i in [
				# self.parameter_current_gen,
				self.parameter_max_gen,
				self.parameter_world_size,
				self.parameter_population_size,
				self.parameter_steps_per_gen,
				self.parameter_genome_size,
				self.parameter_mutation_rate,
				self.parameter_inner_neuron,
			]:
				i.userinput.config(state=tk.DISABLED)
			for i in [
				self.button_apply_param,
				self.button_clearmap,
				self.button_config,
				self.button_export,
				self.button_import,
				self.button_feature1,
				self.button_feature3,
				self.button_save,
			]:
				i.config(state=tk.DISABLED)
			self.updateEvoParamFromController()
			self.evoFrame.feedForwardThread()
		else:
			print("Pause")
			for i in [
				# self.parameter_current_gen,
				self.parameter_max_gen,
				self.parameter_world_size,
				self.parameter_population_size,
				self.parameter_steps_per_gen,
				self.parameter_genome_size,
				self.parameter_mutation_rate,
				self.parameter_inner_neuron,
			]:
				i.userinput.config(state=tk.NORMAL)
			for i in [
				self.button_apply_param,
				self.button_clearmap,
				self.button_config,
				self.button_export,
				self.button_import,
				self.button_feature1,
				self.button_feature3,
				self.button_save,
			]:
				i.config(state=tk.NORMAL)

	def featurebutton(self):
		print("Feature")
		
	def savebutton(self):
		print("Save")

	def importbutton(self):
		print("import")

	def exportbutton(self):
		print("export")

	def configbutton(self):
		self.evoFrame.configbutton()
		print("config")

	def __init__(self,parent,evoFrame,*arg,**kwarg):
		tk.Frame.__init__(self,parent,*arg,**kwarg)
		self.evoFrame=evoFrame
		
		self.label=tk.Label(self,text="Parameters ")
		self.label.pack(side=tk.TOP,fill=tk.X)

		self.parameterFrame=tk.Frame(self,)
		self.parameterFrame.pack(fill=tk.X,padx=10,pady=10)

		self.parameter_current_gen=parameter(self.parameterFrame,text="Current Generation",default_value=0)
		self.parameter_current_gen.pack(fill=tk.X)
		self.parameter_current_gen.userinput.config(state=tk.DISABLED)

		self.parameter_day_count=parameter(self.parameterFrame,text="Day Count ",default_value=0)
		self.parameter_day_count.pack(fill=tk.X)
		self.parameter_day_count.userinput.config(state=tk.DISABLED)

		self.parameter_max_gen=parameter(self.parameterFrame,text="Max Generation",default_value=100)
		self.parameter_max_gen.pack(fill=tk.X)
		
		self.parameter_world_size=parameter(self.parameterFrame,text="World Size",default_value=128)
		self.parameter_world_size.pack(fill=tk.X)

		self.parameter_population_size=parameter(self.parameterFrame,text="Population",default_value=100)
		self.parameter_population_size.pack(fill=tk.X)

		self.parameter_steps_per_gen=parameter(self.parameterFrame,text="Steps Per Generation",default_value=300)
		self.parameter_steps_per_gen.pack(fill=tk.X)

		self.parameter_genome_size=parameter(self.parameterFrame,text="Genome Size",default_value=4)
		self.parameter_genome_size.pack(fill=tk.X)
		
		self.parameter_mutation_rate=parameter(self.parameterFrame,text="Mutation Rate",default_value=0.01)
		self.parameter_mutation_rate.pack(fill=tk.X)
		
		self.parameter_inner_neuron=parameter(self.parameterFrame,text="Inner Neuron",default_value=1)
		self.parameter_inner_neuron.pack(fill=tk.X)

		# self.staticLabelFrame=tk.Frame(self)
		# self.staticLabelFrame.pack(side=tk.BOTTOM,fill=tk.X)

		# self.label1=tk.Label(self.staticLabelFrame,text="Selection Criteria Selected :")
		# self.label1.pack(fill=tk.X,side=tk.LEFT)

		# self.dropdown1s=tk.StringVar()
		# self.dropdown1s.set("Hello world")
		# self.dropdown1=tk.OptionMenu(self.staticLabelFrame,self.dropdown1s,"sdsfd1","sdfsdf2","sdfsdf3")
		# self.dropdown1.pack(side=tk.RIGHT,fill=tk.BOTH)
		

		self.buttomFrame=tk.Frame(self)
		self.buttomFrame.pack(side=tk.BOTTOM,fill=tk.X,padx=10,pady=10)
		
		self.buttomFrameLeft=tk.Frame(self.buttomFrame)
		self.buttomFrameLeft.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)

		self.button_clearmap=tk.Button(self.buttomFrameLeft,text="ClearMap",command=self.clearMap)
		self.button_clearmap.pack(fill=tk.X,pady=2)
		self.button_save=tk.Button(self.buttomFrameLeft,text="Save",command=self.savebutton)
		self.button_save.pack(fill=tk.X,pady=2)
		self.button_import=tk.Button(self.buttomFrameLeft,text="Import",command=self.importbutton)
		self.button_import.pack(fill=tk.X,pady=2)
		self.button_feature1=tk.Button(self.buttomFrameLeft,text="feature1",command=self.featurebutton)
		self.button_feature1.pack(fill=tk.X,pady=2)

		self.buttomFrameMiddle=tk.Frame(self.buttomFrame)
		self.buttomFrameMiddle.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)

		self.button_apply_param=tk.Button(self.buttomFrameMiddle,text="Apply Parameter",command=self.applybutton)
		self.button_apply_param.pack(fill=tk.X,pady=2)
		self.button_export=tk.Button(self.buttomFrameMiddle,text="Export",command=self.exportbutton)
		self.button_export.pack(fill=tk.X,pady=2)
		self.button_config=tk.Button(self.buttomFrameMiddle,text="Config",command=self.configbutton)
		self.button_config.pack(fill=tk.X,pady=2)
		self.button_feature3=tk.Button(self.buttomFrameMiddle,text="feature3",command=self.featurebutton)
		self.button_feature3.pack(fill=tk.X,pady=2)

		self.buttomFrameRight=tk.Frame(self.buttomFrame)
		self.buttomFrameRight.pack(side=tk.RIGHT,fill=tk.BOTH,expand=True)

		self.button_play_pause=ToggleButtonWidget(self.buttomFrameRight,self.playpause,iconpath2="../img/icon/stop-circled-100.png",iconpath1="../img/icon/play-button-100.png")
		self.button_play_pause.pack(side=tk.RIGHT,fill=tk.BOTH,expand=True)

class parameter(tk.Frame):
	def __init__(self,parent,*arg,**kwarg):
		tk.Frame.__init__(self,parent,*arg)

		self.config(padx=10,pady=3)
		self.label=tk.Label(self,text=kwarg["text"],anchor=tk.W)
		self.label.pack(side=tk.LEFT,fill=tk.X,expand=True)

		self.text=tk.StringVar()
		self.text.set(kwarg["default_value"])
		self.userinput=tk.Entry(self,width=10,textvariable=self.text)
		self.userinput.pack(side=tk.RIGHT)
		# self.userinput.insert(0,kwarg["default_value"])

if(__name__=="__main__"):
    root=tk.Tk()
    root.title("Testing LocCanvas")
    root.geometry("650x650")
    root.configure(bg="light grey")
    mat_size=500
    graphFrame=StatusWidget(root,bg=Color.antique_white)
    graphFrame.pack(expand=True,fill=tk.BOTH)

    # print(len(pp),mat_size**2)
    root.mainloop()