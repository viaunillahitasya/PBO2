import requests
import json
class Peminjaman:
    def __init__(self):
        self.__id=None
        self.__id_anggota = None
        self.__id_buku = None
        self.__tanggal_peminjaman = None
        self.__tangal_kembali = None
        self.__url = "http://localhost/perpustakaan/peminjaman_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def id_anggota(self):
        return self.__id_anggota
        
    @id_anggota.setter
    def id_anggota(self, value):
        self.__id_anggota = value
    @property
    def id_buku(self):
        return self.__id_buku
        
    @id_buku.setter
    def id_buku(self, value):
        self.__id_buku = value
    @property
    def tanggal_peminjaman(self):
        return self.__tanggal_peminjaman
        
    @tanggal_peminjaman.setter
    def tanggal_peminjaman(self, value):
        self.__tanggal_peminjaman = value
    @property
    def tangal_kembali(self):
        return self.__tangal_kembali
        
    @tangal_kembali.setter
    def tangal_kembali(self, value):
        self.__tangal_kembali = value
    def get_all(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    def get_by_id_buku(self, id_buku):
        url = self.__url+"?id_buku="+id_buku
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['id']
            self.__id_anggota = item['id_anggota']
            self.__id_buku = item['id_buku']
            self.__tanggal_peminjaman = item['tanggal_peminjaman']
            self.__tangal_kembali = item['tangal_kembali']
        return data
    def simpan(self):
        payload = {
            "id_anggota":self.__id_anggota,
            "id_buku":self.__id_buku,
            "tanggal_peminjaman":self.__tanggal_peminjaman,
            "tangal_kembali":self.__tangal_kembali
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_id_buku(self, id_buku):
        url = self.__url+"?id_buku="+id_buku
        payload = {
            "id_anggota":self.__id_anggota,
            "id_buku":self.__id_buku,
            "tanggal_peminjaman":self.__tanggal_peminjaman,
            "tangal_kembali":self.__tangal_kembali
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_id_buku(self,id_buku):
        url = self.__url+"?id_buku="+id_buku
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text