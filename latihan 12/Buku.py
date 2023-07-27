import requests
import json
class Buku:
    def __init__(self):
        self.__id=None
        self.__kodebuku = None
        self.__judul = None
        self.__kategori = None
        self.__pengarang = None
        self.__penerbit = None
        self.__url = "http://localhost/perpustakaan/buku_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def kodebuku(self):
        return self.__kodebuku
        
    @kodebuku.setter
    def kodebuku(self, value):
        self.__kodebuku = value
    @property
    def judul(self):
        return self.__judul
        
    @judul.setter
    def judul(self, value):
        self.__judul = value
    @property
    def kategori(self):
        return self.__kategori
        
    @kategori.setter
    def kategori(self, value):
        self.__kategori = value
    @property
    def pengarang(self):
        return self.__pengarang
        
    @pengarang.setter
    def pengarang(self, value):
        self.__pengarang = value
    @property
    def penerbit(self):
        return self.__penerbit
        
    @penerbit.setter
    def penerbit(self, value):
        self.__penerbit = value
    def get_all(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    def get_by_kodebuku(self, kodebuku):
        url = self.__url+"?kodebuku="+kodebuku
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['id']
            self.__kodebuku = item['kodebuku']
            self.__judul = item['judul']
            self.__kategori = item['kategori']
            self.__pengarang = item['pengarang']
            self.__penerbit = item['penerbit']
        return data
    def simpan(self):
        payload = {
            "kodebuku":self.__kodebuku,
            "judul":self.__judul,
            "kategori":self.__kategori,
            "pengarang":self.__pengarang,
            "penerbit":self.__penerbit
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_kodebuku(self, kodebuku):
        url = self.__url+"?kodebuku="+kodebuku
        payload = {
            "kodebuku":self.__kodebuku,
            "judul":self.__judul,
            "kategori":self.__kategori,
            "pengarang":self.__pengarang,
            "penerbit":self.__penerbit
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_kodebuku(self,kodebuku):
        url = self.__url+"?kodebuku="+kodebuku
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text