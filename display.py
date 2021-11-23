import tkinter as tk

root=tk.Tk()
root.title("Evolution Using Selection")
root.geometry("800x580")
# root.iconphoto("iconpath")
root.minsize(560,360)

mainFrame=tk.Frame(root,bg="lightgreen")
mainFrame.pack(fill=tk.BOTH,expand=True)

# genFrame=tk.Frame(mainFrame,bg="lightgrey")
# genFrame.pack()


root.mainloop()