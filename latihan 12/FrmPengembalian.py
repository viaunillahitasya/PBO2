import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Pengembalian import *
class FrmPengembalian:
    
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
        Label(mainFrame, text='ID_ANGGOTA:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='ID_BUKU:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='TANGGAL_PENGEMBALIAN:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='DENDA:').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        # Textbox
        self.txtId_anggota = Entry(mainFrame) 
        self.txtId_anggota.grid(row=0, column=1, padx=5, pady=5)
        # Textbox
        self.txtId_buku = Entry(mainFrame) 
        self.txtId_buku.grid(row=1, column=1, padx=5, pady=5)
        self.txtId_buku.bind("<Return>",self.onCari) # menambahkan event Enter key
        # Textbox
        self.txtTanggal_pengembalian = Entry(mainFrame) 
        self.txtTanggal_pengembalian.grid(row=2, column=1, padx=5, pady=5)
        # Textbox
        self.txtDenda = Entry(mainFrame) 
        self.txtDenda.grid(row=3, column=1, padx=5, pady=5)
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        # define columns
        columns = ('id','id_anggota','id_buku','tanggal_pengembalian','denda')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id', text='ID')
        self.tree.column('id', width="30")
        self.tree.heading('id_anggota', text='ID_ANGGOTA')
        self.tree.column('id_anggota', width="30")
        self.tree.heading('id_buku', text='ID_BUKU')
        self.tree.column('id_buku', width="30")
        self.tree.heading('tanggal_pengembalian', text='TANGGAL_PENGEMBALIAN')
        self.tree.column('tanggal_pengembalian', width="30")
        self.tree.heading('denda', text='DENDA')
        self.tree.column('denda', width="30")
        # set tree position
        self.tree.place(x=0, y=200)
        
    def onClear(self, event=None):
        self.txtId_anggota.delete(0,END)
        self.txtId_anggota.insert(END,"")
        self.txtId_buku.delete(0,END)
        self.txtId_buku.insert(END,"")
        self.txtTanggal_pengembalian.delete(0,END)
        self.txtTanggal_pengembalian.insert(END,"")
        self.txtDenda.delete(0,END)
        self.txtDenda.insert(END,"")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data pengembalian
        obj = Pengembalian()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["id"],d["id_anggota"],d["id_buku"],d["tanggal_pengembalian"],d["denda"]))
    def onCari(self, event=None):
        id_buku = self.txtId_buku.get()
        obj = Pengembalian()
        a = obj.get_by_id_buku(id_buku)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        id_buku = self.txtId_buku.get()
        obj = Pengembalian()
        res = obj.get_by_id_buku(id_buku)
        self.txtId_anggota.delete(0,END)
        self.txtId_anggota.insert(END,obj.id_anggota)
        self.txtId_buku.delete(0,END)
        self.txtId_buku.insert(END,obj.id_buku)
        self.txtTanggal_pengembalian.delete(0,END)
        self.txtTanggal_pengembalian.insert(END,obj.tanggal_pengembalian)
        self.txtDenda.delete(0,END)
        self.txtDenda.insert(END,obj.denda)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from input
        id_anggota = self.txtId_anggota.get()
        id_buku = self.txtId_buku.get()
        tanggal_pengembalian = self.txtTanggal_pengembalian.get()
        denda = self.txtDenda.get()
        # create new Object
        obj = Pengembalian()
        obj.id_anggota = id_anggota
        obj.id_buku = id_buku
        obj.tanggal_pengembalian = tanggal_pengembalian
        obj.denda = denda
        if(self.ditemukan==False):
            # save the record
            res = obj.simpan()
        else:
            # update the record
            res = obj.update_by_id_buku(id_buku)
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        #clear the form input
        self.onClear()
    def onDelete(self, event=None):
        id_buku = self.txtId_buku.get()
        obj = Pengembalian()
        obj.id_buku = id_buku
        if(self.ditemukan==True):
            res = obj.delete_by_id_buku(id_buku)
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
    aplikasi = FrmPengembalian(root2, "Aplikasi Data Pengembalian")
    root2.mainloop()
