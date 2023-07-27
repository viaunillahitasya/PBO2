from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,W

class FrmAdmin2:
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("400x200")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        # pasang Label
        Label(mainFrame, text='Admin-2',font=("Arial", 40)).grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        
               
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()  
    aplikasi = FrmAdmin2(root, "Admin-2")
    root.mainloop() 