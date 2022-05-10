import tkinter as tk

# import sys
# sys.path.append('../src')

# from creature import Creature
# from genome import Genome

from color import Color


class ToggleButtonWidget(tk.Button):

    def __init__(self,parent,command,text1:str="",iconpath1:str=None,text2:str="",iconpath2:str=None,icon_side:str=tk.LEFT,*arg,**kwarg):
        self.image1=tk.PhotoImage(file=iconpath1)
        self.image2=tk.PhotoImage(file=iconpath2)
        self.text=tk.StringVar()
        self.userfunction=command
        self.text.set(text1)
        self.text1=text1
        self.text2=text2
        tk.Button.__init__(self,parent,textvariable=self.text,image=self.image1,compound=icon_side,command=self.toggle,*arg,**kwarg,bd=0,relief=tk.SUNKEN)
        # tk.Button.__init__(self,parent,text="hello",*arg,**kwarg)
        
        self.toggle_flag=True

    def toggle(self):
        self.userfunction()
        if(self.toggle_flag==True):
            self.toggle_flag=False
            self.config(image=self.image2)
            self.text.set(self.text2)

        else:
            self.toggle_flag=True
            self.config(image=self.image1)
            self.text.set(self.text1)

class CustomButtonWidget(tk.Button):

    def __init__(self,parent,*arg,**kwarg):
        tk.Button.__init__(self,parent,*arg,**kwarg)
        self.config(background=Color.sea_green)

if(__name__=="__main__"):
    root=tk.Tk()
    root.title("Testing LocCanvas")
    root.geometry("650x650")
    root.configure(bg="light grey")
    mat_size=500
    # frame = tk.Frame(root)
    # frame.pack()
    # graphFrame=ToggleButtonWidget(frame,"on","../img/icon/pause-button-100.png","off","../img/icon/play-button-100.png")
    graphFrame=ToggleButtonWidget(root,iconpath1="../img/icon/pause-button-100.png",iconpath2="../img/icon/play-button-100.png")
    graphFrame.pack()

    print(mat_size**2)
    root.mainloop()