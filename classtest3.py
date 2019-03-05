#!/usr/bin/env python3
#-*-coding:utf-8-*-

class UserData:
	def __init__(self, user_id, user_name):
		self.id = user_id
		self._name = user_name
	def __repr__(self):
		return 'ID:{} Name:{}'.format(self.id,self.name)
class NewUser(UserData):
	@property
	def name(self):
	    return self._name
	@name.setter
	def name(self,value):
		if len(value) > 3:
			self._name = value
		else:
			print('Error')
	

	
if  __name__ == '__main__':
	user1 = NewUser(101, 'Jack')
	user1.name = 'Lou'
	user1.name = 'Jackie'
	
	user2 = NewUser(102, 'Louplus')
	#print(user1)
	#print(user2)
	#print(NewUser.get_group())
	#print(NewUser.format_userdata(109,'Lucy'))
	print(user1.name)
	print(user2.name)

	
