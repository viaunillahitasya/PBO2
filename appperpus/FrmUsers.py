import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Users import *
class FrmUsers:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("450x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        Label(mainFrame, text='USERNAME:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='PASSWD:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='ROLENAME:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        # Textbox
        self.txtUsername = Entry(mainFrame) 
        self.txtUsername.grid(row=0, column=1, padx=5, pady=5)
        self.txtUsername.bind("<Return>",self.onCari) # menambahkan event Enter key
        # Textbox
        self.txtPasswd = Entry(mainFrame) 
        self.txtPasswd.grid(row=1, column=1, padx=5, pady=5)
        # Combo Box
        self.txtRolename = StringVar()
        Cbo_rolename = ttk.Combobox(mainFrame, width = 17, textvariable = self.txtRolename) 
        Cbo_rolename.grid(row=2, column=1, padx=5, pady=5)
        # Adding rolename combobox drop down list
        Cbo_rolename['values'] = ('admin','dosen','mahasiswa')
        Cbo_rolename.current()
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        # define columns
        columns = ('id','username','passwd','rolename')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id', text='ID')
        self.tree.column('id', width="30")
        self.tree.heading('username', text='USERNAME')
        self.tree.column('username', width="30")
        self.tree.heading('passwd', text='PASSWD')
        self.tree.column('passwd', width="30")
        self.tree.heading('rolename', text='ROLENAME')
        self.tree.column('rolename', width="30")
        # set tree position
        self.tree.place(x=0, y=200)
        
    def onClear(self, event=None):
        self.txtUsername.delete(0,END)
        self.txtUsername.insert(END,"")
        self.txtPasswd.delete(0,END)
        self.txtPasswd.insert(END,"")
        self.txtRolename.set("")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data users
        obj = Users()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["id"],d["username"],d["passwd"],d["rolename"]))
    def onCari(self, event=None):
        username = self.txtUsername.get()
        obj = Users()
        a = obj.get_by_username(username)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        username = self.txtUsername.get()
        obj = Users()
        res = obj.get_by_username(username)
        self.txtUsername.delete(0,END)
        self.txtUsername.insert(END,obj.username)
        self.txtPasswd.delete(0,END)
        self.txtPasswd.insert(END,obj.passwd)
        self.txtRolename.set(obj.rolename)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from input
        username = self.txtUsername.get()
        passwd = self.txtPasswd.get()
        rolename = self.txtRolename.get()
        # create new Object
        obj = Users()
        obj.username = username
        obj.passwd = passwd
        obj.rolename = rolename
        if(self.ditemukan==False):
            # save the record
            res = obj.simpan()
        else:
            # update the record
            res = obj.update_by_username(username)
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        #clear the form input
        self.onClear()
    def onDelete(self, event=None):
        username = self.txtUsername.get()
        obj = Users()
        obj.username = username
        if(self.ditemukan==True):
            res = obj.delete_by_username(username)
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        
        self.onClear()
            
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()
if __name__ == '__main__':
    root2 = tk.Tk()
    aplikasi = FrmUsers(root2, "Aplikasi Data Users")
    root2.mainloop()