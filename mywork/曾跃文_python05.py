#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-05 20:34:21
# @Author  : zengyw (1004324878@qq.com)
# @Link    : ${link}
# @Version : $Id$


"""
要求大家用面向对象的设计编写一个python程序，实现一个文字游戏系统。

动物园里面有10个房间，房间号从1 到 10。

每个房间里面可能是体重200斤的老虎或者体重100斤的羊。
游戏开始后，系统随机在10个房间中放入老虎或者羊。
b
然后随机给出房间号，要求游戏者选择敲门还是喂食。

如果选择喂食：
喂老虎应该输入单词 meat，喂羊应该输入单词 grass
喂对了，体重加10斤。 喂错了，体重减少10斤

如果选择敲门：
敲房间的门，里面的动物会叫，老虎叫会显示 ‘Wow !!’,羊叫会显示 ‘mie~~’。 动物每叫一次体重减5斤。


游戏者强记每个房间的动物是什么，以便不需要敲门就可以喂正确的食物。 
游戏3分钟结束后，显示每个房间的动物和它们的体重。


实现过程中，有什么问题，请通过课堂上讲解的调试方法，尽量自己发现错误原因。


分析
1 老虎类：Tiger()
		属性：体重：weight

		方法	：叫喊：roar（）
			  喂食：feed（）
			  敲门：knock（）

随机获取一个房间：
猜里面的动物，yourguessanimal = input（请输入tiger或者sheep：）

将输入的动物实例化
if yourguessanimal == 'tiger'
    yourguessanimal = Tiger()

与房间内随机生成的动物匹配
匹配成功，房间里面的动物增加相应的体重，匹配不成功，则减少相应的体重

根据输入的动物调用方法



"""
from random import randint
import time


class Tiger:
	"""docstring for Tiger"""
	classname = 'tiger'

	def __init__(self, weight = 200):
		self.weight = weight

	def roar(self):    #老虎的叫声
		print("wow!!!")
		self.weight -= 5

	def feed(self,food):  #老虎喂食
		self.food = food
		if self.food == 'meat':
			self.weight += 10
			print('正确，体重 + 10')
		else:
			self.weight -= 10
			print('太惨了，体重 - 10')

class Sheep:
	"""docstring for Tiger"""
	classname = 'sheep'
	
	def __init__(self, weight = 100):
		self.weight = weight

	def roar(self):
		print("mie~~")
		self.weight -= 5

	def feed(self,food):
		self.food = food
		if self.food == 'grass':
			self.weight += 10
			print('正确，体重 + 10')
		else:
			self.weight -= 10
			print('太惨了，体重 - 10')

class Room:
	def __init__(self,num,animal):
		self.num = num
		self.animal = animal


#将房间的编号以及里面的动物设定
rooms = []
for no in range(0,10):
	if randint(0,1):
		ani = Tiger(200)
	else:
		ani = Sheep(100)

	room = Room(no,ani)
	rooms.append(room)

#引入计时器
starttime = time.time()
while True:
	curTime = time.time()
	if (curTime - starttime) > 120:
		print('\n\ntime is up,game over\n\n')
		for idx,room in enumerate(rooms):
			print('房间：%s'%(idx + 1),room.animal.classname,room.animal.weight)
		break

	roomno = randint(1,10)
	room = rooms[roomno-1]  #因为房间编号是从0开始
	ch = input('欢迎来到房间%s 门前，要敲门吗？[y/n]' %roomno)

	if ch == 'y':
		room.animal.roar()

	food = input('请给房间中的动物喂食：（meat or grass）')
	room.animal.feed(food.strip())























# if __name__ == '__main__':
	# 
	# from random import randint,choice
	# number = randint(1,10)
	# print(number)
	# systemchioce = choice([Tiger(),Sheep()])
	# print(systemchioce)
	# choiceroom = Room(number,systemchioce)
	# import time
	# start = time.clock()
	# while True:
		# end = time.clock()
	# 输入一种动物，并将输入的动物实例化
	# print("请猜房间里面的动物，输入tiger或者sheep：") 
	# while True:
		# guessanimal = input('\n')
		# if guessanimal == 'tiger':
			# guessanimal = Tiger()
			# break
		# elif guessanimal == 'sheep':
			# guessanimal = Sheep()
			# break
		# else:
			# print("请输入tiger或者sheep")

	# 将实例化后的动物与系统随机生成的房间内动物匹配,并调用动物相应的方法
		# 
	# if guessanimal == systemchioce:
		# guessanimal.feed('meat')
	# else:
		# print('猜错了，房间的动物是%s哦' %systemchioce)
		# guessanimal.knock()

	# guessanimal_weight = guessanimal.weight

	# roomlist = []
	# for number in range(1,11):
		# finalweight = {}
		# finalweight['roomnumber'] = number
		# finalweight['weight'] = guessanimal.weight
	# roomlist.append(finalweight)


	# {'roomnuber':number,'weight':guessanimal.weight}
	# import pprint
	# pprint.pprint(roomlist)




	# 
# print(choiceroom.num)
	# print(choiceroom.animal.weight)

