import tkinter as tk
class View(tk.Frame):
    count=0
    objList=[]
    def __init__(self,parent,*arg,**kwarg):
        pass
    
    def __widgetInit(self,parent,*arg,**kwarg):
        tk.Frame.__init__(self,parent,*arg,**kwarg)
        self.widgetType="View"
        self.children={}

class Frame(tk.Frame):
    count=0
    objList=[]
    def __init__(self,parent,*arg,**kwarg):
        pass
    
    def __widgetInit(self,parent,*arg,**kwarg):
        tk.Frame.__init__(self,parent,*arg,**kwarg)
        self.widgetType="Frame"

class Img(tk.PhotoImage):
    count=0
    objList=[]
    def __init__(self,file_path,*arg,**kwarg):
        pass

    
    def __widgetInit(self,file_path,*arg,**kwarg):
        tk.PhotoImage.__init__(self,*arg,**kwarg)
        self.widgetType="PhotoImage"
        self.path=file_path

class WidgetHandler(tk.Tk,View,Img,Frame):
    def __init__(self,title,size=(800,590),min_size=(560,360),favicon_path=None,*arg,**kwarg):
        tk.Tk.__init__(self,*arg,**kwarg)
        self.view={"count":0}
        self.myimg={"count":0}
        self.icon={"count":0}

        self.canavas={"count":0}
        self.frame={"count":0}
        self.label={"count":0}
        self.button={"count":0}
        self.icon_button={"count":0}


        self.title(title)
        self.geometry("x".join([str(i) for i in size]))
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.minsize(*min_size)
        if (favicon_path!=None):
            self.iconphoto(False, self.set_img(favicon_path,"small"))
            # self.iconbitmap( dir_path+"logo1.png")
    
    def set_canavas(self,parent,canavas_id=None,**arg)->dict:
        self.__id_exist_check(self.canavas,canavas_id)
        if (canavas_id==None):canavas_id="canavas"+str(self.canavas["count"])
        self.canavas[canavas_id]={}
        self.canavas[canavas_id]["widgetType"]="Canavas"
        self.canavas[canavas_id]["widget"]=tk.Canvas(parent["widget"],**arg)
        self.canavas[canavas_id]["frame_count"]=0
        self.canavas["count"]+=1
        return self.canavas[canavas_id]
    
    def set_canavas_custom_frame1(self,parent_canavas,frame_id=None,height=10,width=10,spacing=10,**arg):
        tmp=self.set_frame(parent_canavas,frame_id,**arg)
        tmp["widgetType"]="Canavas Frame"
        tmp["index"]=parent_canavas["frame_count"]
        tmp["height"]=height
        tmp["width"]=width
        tmp["spacing"]=spacing
        tmp["xy"]=(0,tmp["index"]*(height+spacing))
        parent_canavas["widget"].create_window(tmp["xy"],window=tmp["widget"],anchor=tk.NW,width=width,height=height)
        parent_canavas["frame_count"]+=1
        return tmp

    def set_view(self,view_id,**arg)->None:
        self.__id_exist_check(self.view,view_id)
        self.view[view_id]={}
        self.view[view_id]["widgetType"]="View"
        self.view[view_id]["widget"]=tk.Frame(self,**arg)
        self.view[view_id]["widget"].grid(row=0,column=0,sticky=tk.N+tk.E+tk.W+tk.S,)
        self.view["count"]+=1
        # return self.view[view_id]
        self.root[view_id]=self.view[view_id]

    def set_frame(self,parent,frame_id=None,**arg)->dict:
        self.__id_exist_check(self.frame,frame_id)
        if (frame_id==None):frame_id="frame"+str(self.frame["count"])
        self.frame[frame_id]={}
        self.frame[frame_id]["widgetType"]="Frame"
        self.frame[frame_id]["widget"]=tk.Frame(parent["widget"],**arg)
        self.frame["count"]+=1
        return self.frame[frame_id]
 
    def set_img(self,file_path,size="medium")->tk.PhotoImage:
        """set_img(file_path,size=["root","small","medium","large","custom"]"""
        image_name=file_path.split("/")[-1].split(".")[0]
        try:
            tmp=self.myimg[image_name]
            try:
                return tmp[size]
            except (KeyError):
                if(size=="small"):
                    self.myimg[image_name]["small"]=self.myimg[image_name]["widget"].subsample(4)
                elif(size=="medium"):
                    self.myimg[image_name]["medium"]=self.myimg[image_name]["widget"].subsample(2)
                elif(size=="large"):
                    self.myimg[image_name]["large"]=self.myimg[image_name]["widget"].zoom(3).subsample(4)
                elif(size=="root"):
                    return self.myimg[image_name]["widget"]
                elif(size=="custom"):
                    try:
                        return self.myimg[image_name]["custom"]
                    except KeyError:
                        raise ValueError(size,"size needs to assigned manually")
                else:
                    raise ValueError(size," not a valid key ,Key must be from [root,small,medium,large]")
                return self.myimg[image_name][size]

        except (KeyError):
            self.myimg[image_name]={}
            self.myimg[image_name]["widgetType"]="PhotoImage"
            self.myimg[image_name]["widget"]=tk.PhotoImage(file=file_path)
            self.myimg[image_name]["path"]=file_path
            self.myimg["count"]+=1
            return self.set_img(file_path,size)

    def set_icon(self,parent,icon_path,size="small",icon_id=None,**arg)->dict:
        self.__id_exist_check(self.icon,icon_id)
        if(icon_id==None):icon_id="icon"+str(self.icon["count"])
        self.icon[icon_id]={}
        self.icon[icon_id]["widgetType"]="Icon"
        self.icon[icon_id]["widget"]=tk.Label(parent["widget"],image=self.set_img(icon_path,size),**arg)
        self.icon[icon_id]["imgKey"]=icon_path.split("/")[-1].split(".")[0]
        self.icon["count"]+=1
        return self.icon[icon_id]

    def set_label(self,parent,label_message,label_id=None,**arg)->dict:
        self.__id_exist_check(self.label,label_id)
        if(label_id==None):label_id="label"+str(self.label["count"])
        self.label[label_id]={}
        self.label[label_id]["widgetType"]="Label"
        self.label[label_id]["labelText"]=tk.StringVar(parent["widget"],label_message,label_message)
        self.label[label_id]["widget"]=tk.Label(parent["widget"],textvariable=self.label[label_id]["labelText"],**arg)
        self.label["count"]+=1
        return self.label[label_id]
 
    def set_button(self,parent,text,button_id=None,**arg)->dict:
        self.__id_exist_check(self.button,button_id)
        if(button_id==None):button_id="button"+str(self.button["count"])
        self.button[button_id]={}
        self.button[button_id]["widgetType"]="Button"
        self.button[button_id]["buttonText"]=tk.StringVar(parent["widget"],text,button_id)
        self.button[button_id]["widget"]=tk.Button(parent["widget"],textvariable=self.button[button_id]["buttonText"],**arg)
        self.button["count"]+=1
        return self.button[button_id]

    def set_icon_button(self,parent,button_text,icon_path,button_id=None,icon_size="small",icon_side=tk.LEFT,space_btw=0,**arg)->dict:
        self.__id_exist_check(self.icon_button,button_id)
        button_text=space_btw*" "+button_text
        if(button_id==None):button_id="icon_button"+str(self.icon_button["count"])
        self.icon_button[button_id]={}
        self.icon_button[button_id]["widgetType"]="IconButton"
        self.icon_button[button_id]["buttonText"]=tk.StringVar(parent["widget"],button_text,button_text)
        self.icon_button[button_id]["widget"]=tk.Button(
            parent["widget"],
            textvariable=self.icon_button[button_id]["buttonText"],
            image=self.set_img(icon_path,icon_size),
            compound=icon_side,
            **arg
        )
        self.icon_button["count"]+=1
        return self.icon_button[button_id]
    
    def __id_exist_check(self,variable,id)->bool:
        try:
            variable[id]
            raise Exception(id ," id already exist(id must be unique)")
        except KeyError:
            # "Not Exist"
            return True 

    def get_root(self)->dict:
        return self.root
    
    def get_view(self)->dict:
        return self.view
    
    def get_frame(self)->dict:
        return self.frame

    def get_canavas(self)->dict:
        return self.canavas
    
    def get_label(self)->dict:
        return self.label
    
    def get_icon(self)->dict:
        return self.icon
    
    def get_img(self)->dict:
        return self.myimg
    
    def get_icon_button(self)->dict:
        return self.icon_button
    
    def get_button(self,)->dict:
        return self.button

    def get_all(self)->dict:
        return {
            "root":self.get_root(),
            "view":self.get_view(),
            "frame":self.get_frame(),
            "canavas":self.get_canavas(),
            "icon":self.get_icon(),
            "img":self.get_img(),
            "label":self.get_label(),
            "button":self.get_button(),
            "icon_button":self.get_icon_button(),
        }
        

if __name__=="__main__":
    master=WidgetHandler("Testing",(800,560),(560,360),"../img/icon/logo1.png")
    master.mainloop()