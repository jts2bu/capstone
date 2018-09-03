import tkinter as tk
from tkinter import *

complete = True

class uvaAnalytics(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.minsize(width=350, height=350)

        container = tk.Frame(self)

        container.pack(side="top", fill ="both", expand = "true")
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}

        for F in (WelcomePage, SignPage, FinishPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(WelcomePage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        if isinstance(cont, FinishPage):
            cont.updatepage(complete)
        frame.tkraise()
    
class WelcomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        img = PhotoImage(file="uva-logo.gif")
        rotunda = tk.Label(self, image=img)
        rotunda.img = img
        rotunda.pack(side = "top")
        # rotunda.grid(row = 0, columnspan = 2)

        title = tk.Label(self, text="Virginia Analytics", font=('Helvetica', 24))
        title.pack(side = "top")
        # title.grid(row = 1, columnspan = 2)

        warning = tk.Label(self, text="this service is in development and may not function properly \n use with caution", font = ('Helvetica', 8))
        warning.pack(side = "top")
        # warning.grid(row = 2, columnspan = 2)
        
        butt = tk.Button(self, text = "Enter", command = lambda: controller.show_frame(SignPage))
        #butt2 = tk.Button(self,text = "Quit", command = lambda: quit())
        butt.pack(side = "top")
        #butt2.pack(side='left')
        
        # butt.grid(column = 0, row = 3, sticky="E")
        # butt2.grid(column = 1, row = 3, sticky="W")


class SignPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        img = PhotoImage(file="uva-logo.gif")
        rotunda = tk.Label(self, image=img)
        rotunda.img = img
        rotunda.pack(side = "top")

        entry = tk.Entry(self)
        entry.bind("<Return>", (lambda event: self.sendData(entry, controller)))
        entry.pack(side = 'top')
    
    def sendData(self, entry, controller):
        print(entry.get())
        entry.delete(0, 'end')
        complete = False
        controller.show_frame(FinishPage)

        ### construct the page in this method and display it?
        ### how to pass information from different TKinter frames

class FinishPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        ret = tk.Button(self, text = "Return", command = lambda: controller.show_frame(SignPage))
        ret.pack(side="top")
    
    def updatepage(self, status):
        status = tk.Label(self, text = status)
        status.pack(side="top")


        
    

app = uvaAnalytics()
app.mainloop()
