import requests
import json
class Users:
    def __init__(self):
        self.__id=None
        self.__username = None
        self.__passwd = None
        self.__rolename = None
        self.__url = "http://localhost/appakademik/users_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def username(self):
        return self.__username
        
    @username.setter
    def username(self, value):
        self.__username = value
    @property
    def passwd(self):
        return self.__passwd
        
    @passwd.setter
    def passwd(self, value):
        self.__passwd = value
    @property
    def rolename(self):
        return self.__rolename
        
    @rolename.setter
    def rolename(self, value):
        self.__rolename = value
    def get_all(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    def get_by_username(self, username):
        url = self.__url+"?username="+username
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['id']
            self.__username = item['username']
            self.__passwd = item['passwd']
            self.__rolename = item['rolename']
        return data
    def simpan(self):
        payload = {
            "username":self.__username,
            "passwd":self.__passwd,
            "rolename":self.__rolename
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_username(self, username):
        url = self.__url+"?username="+username
        payload = {
            "username":self.__username,
            "passwd":self.__passwd,
            "rolename":self.__rolename
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_username(self,username):
        url = self.__url+"?username="+username
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text
    
    def Login(self):
        payload = {
            "username":self.__username,
            "passwd":self.__passwd
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text