import random
import tkinter as tk
from evolution import Evolution

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
			print(self.frames[F])

		# self.show_frame(ExitPage)
		self.show_frame(HomePage)
	
	def show_frame(self,widget):
		self.frames[widget].tkraise()

class HomePage(tk.Frame):

	def __init__(self,parent:tk.Frame,controllerFrame:tk.Tk,*arg,**kwarg):
		tk.Frame.__init__(self,parent,*arg,**kwarg,bg="light grey")
		self.configure(padx=10,pady=10)

		# Location Graph
		graphFrame=tk.Frame(self,background="green")
		graphFrame.pack(side=tk.LEFT ,fill=tk.BOTH)
		
		# Above Graph
		locGraph=tk.Frame(graphFrame,bg="pink",height=600,width=600)
		locGraph.pack(side=tk.TOP)


class ExitPage(tk.Frame):

	def __init__(self,parent,controllerFrame,*arg,**kwarg):
		tk.Frame.__init__(self,parent,*arg,**kwarg,bg="light pink")
		self.configure(padx=10,pady=10)


app=Simulator()
app.mainloop()