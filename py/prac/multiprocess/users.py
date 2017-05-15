#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Users(object):
    """所有玩家的集合,负责玩家登陆,同时实例化每一个玩家,放在列表中
    并接受每个玩家的请求,用多线程"""
    def __init__(self, *args, **kwargs):
        __usrs = {}  #玩家集合
        return super(Users, self).__init__(*args, **kwargs)

    def add_user(self, usr):
    	self.__usrs[usr.name] = usr

    def remove_user(self, usr):
    	if usr.name in self.__usrs.keys():
    		del self.__usrs[usr.name]









class User(object):
    """一个玩家，包括玩家的物品，任务进度，位置，血量，装备等所有信息"""
    def __init__(self, name, password):
    	
    	self.__name = name
    	self.__password = password
    	self.__blood_value = 10000
    	self.__position = ()
    	self.__mission = {}
    	self.__equipment = []
    	self.__drug = {}
    	self.__other_goods = {}


   
    def get_name(self):
        return self.__name
       
    def set_name(self, value):
        self.__name = value
    
    def check_password(self, password):
    	if (self.__password == password):
    		return True
    	else:
    		return False




    

if  __name__ == "__main__":
	
	user = User("hello", "12345");
	userName = user.get_name();
	print userName

