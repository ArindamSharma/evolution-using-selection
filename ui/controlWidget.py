from email.policy import default
import tkinter as tk

# import sys
# sys.path.append('../src')

# from creature import Creature
# from genome import Genome

from color import Color
from buttonWidget import ToggleButtonWidget

class StatusWidget(tk.Frame):
	def __init__(self,parent,*arg,**kwarg):
		tk.Frame.__init__(self,parent,*arg,**kwarg)
		
		self.label=tk.Label(self,text="Parameters ")
		self.label.pack(side=tk.TOP,fill=tk.X)

		self.parameterFrame=tk.Frame(self,)
		self.parameterFrame.pack(fill=tk.X)

		self.parameter1=parameter(self.parameterFrame,text="Current Generation",default_value=0)
		self.parameter1.pack(fill=tk.X)
		
		self.parameter2=parameter(self.parameterFrame,text="World Size",default_value=128)
		self.parameter2.pack(fill=tk.X)

		self.parameter3=parameter(self.parameterFrame,text="Population",default_value=1000)
		self.parameter3.pack(fill=tk.X)

		self.parameter4=parameter(self.parameterFrame,text="Steps Per Generation",default_value=300)
		self.parameter4.pack(fill=tk.X)

		self.parameter5=parameter(self.parameterFrame,text="Genome Size",default_value=4)
		self.parameter5.pack(fill=tk.X)
		
		self.parameter6=parameter(self.parameterFrame,text="Mutation Rate",default_value=0.01)
		self.parameter6.pack(fill=tk.X)
		
		self.parameter6=parameter(self.parameterFrame,text="Inner Neuron",default_value=1)
		self.parameter6.pack(fill=tk.X)

		self.staticLabelFrame=tk.Frame(self)
		self.staticLabelFrame.pack(side=tk.BOTTOM,fill=tk.X)

		self.label1=tk.Label(self.staticLabelFrame,text="Selection Criteria Selected :")
		self.label1.pack(fill=tk.X,side=tk.LEFT)

		self.dropdown1s=tk.StringVar()
		self.dropdown1s.set("Hello world")
		self.dropdown1=tk.OptionMenu(self.staticLabelFrame,self.dropdown1s,"sdsfd1","sdfsdf2","sdfsdf3")
		self.dropdown1.pack(side=tk.RIGHT,fill=tk.BOTH)
		

		self.buttomFrame=tk.Frame(self)
		self.buttomFrame.pack(side=tk.BOTTOM,fill=tk.X)
		
		self.buttomFrameLeft=tk.Frame(self.buttomFrame)
		self.buttomFrameLeft.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)

		self.button2=tk.Button(self.buttomFrameLeft,text="Save")
		self.button2.pack(fill=tk.X)
		self.button1=tk.Button(self.buttomFrameLeft,text="Import")
		self.button1.pack(fill=tk.X)
		self.button1=tk.Button(self.buttomFrameLeft,text="feature1")
		self.button1.pack(fill=tk.X)

		self.buttomFrameMiddle=tk.Frame(self.buttomFrame)
		self.buttomFrameMiddle.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)

		self.button2=tk.Button(self.buttomFrameMiddle,text="Update Parameter")
		self.button2.pack(fill=tk.X)
		self.button2=tk.Button(self.buttomFrameMiddle,text="Export")
		self.button2.pack(fill=tk.X)
		self.button2=tk.Button(self.buttomFrameMiddle,text="Config")
		self.button2.pack(fill=tk.X)

		self.buttomFrameRight=tk.Frame(self.buttomFrame)
		self.buttomFrameRight.pack(side=tk.RIGHT,fill=tk.BOTH,expand=True)

		self.button1=ToggleButtonWidget(self.buttomFrameRight,iconpath1="../img/icon/pause-button-100.png",iconpath2="../img/icon/play-button-100.png")
		self.button1.pack(side=tk.RIGHT,fill=tk.BOTH,expand=True)

class parameter(tk.Frame):
	def __init__(self,parent,*arg,**kwarg):
		tk.Frame.__init__(self,parent,*arg)

		self.config(padx=10)
		self.label=tk.Label(self,text=kwarg["text"],anchor=tk.W)
		self.label.pack(side=tk.LEFT,fill=tk.X,expand=True)

		self.userinput=tk.Entry(self,width=10)
		self.userinput.pack(side=tk.RIGHT)
		self.userinput.insert(0,kwarg["default_value"])

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