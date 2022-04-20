import tkinter as tk
from tk_widget_handler import WidgetHandler

app=WidgetHandler()
app.set_root("Evolution Using Selection ",)
app.set_view("Home",bg="light green")
app.view["Home"]["LocGraph"]=app.set_frame(app.view["Home"],bg="blue")
app.view["Home"]["LocGraph"]["root"].pack(fill=tk.BOTH,expand=tk.FALSE)

app.printJson()


app.mainloop()