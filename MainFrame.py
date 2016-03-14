import tkinter as tk
from WCanv import G3Dcnv
from MCanv import M3Dcnv

def modifyWL(widlist): # names from widget list ---> to classes without initializing ()
    toplabelsToRun=[]
    for wid in widlist:
        if wid=='geometry': toplabelsToRun.append(G3Dcnv)
        if wid=='mesh': toplabelsToRun.append(M3Dcnv)

    return toplabelsToRun
        
class PrintConsole:
    def __init__(self,master):
            self.console=tk.Text(master,width = 80,height = 2)
            self.console.insert('1.0','RapTorus v1.16.0304 ; (console output)')
            self.console.pack()

class MFrame:
    def __init__(self,c):
        self.root = tk.Tk()
        self.root.wm_title("RapTorus")
        #self.root.withdraw() # hiding main window <--------------(open it when more base func is added)
        console=PrintConsole(self.root).console
        self.toplist=[]
        self.widgets=[]
        for cons in c:
            tLTR=modifyWL(cons.Gwidgets) 
            for TL in tLTR:
                self.toplist.append(tk.Toplevel(self.root))
            for tlw in self.toplist:
                self.widgets.append(TL(cons,tlw))
        
        for wdgt in self.widgets:
            wdgt.canvas.pack()
        self.root.mainloop()

        #move constants to main frame and push model and cmass and so on there/
        #also hide initialization of cons to exporting module
