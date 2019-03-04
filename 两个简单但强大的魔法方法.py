# __init__():创建对象时自动调用
# __str__(): 打印对象时调用，显示对象的描述信息


class Cat(object):
	"""docstring for Cat"""
	def __init__(self, name, age):		
		self.name = name
		self.age = age

	def __str__(self):  
    # 不要忘了这里的self参数，否则调用时会报异常： __str__() takes 0 positional arguments but 1 was given
		return "%s的年龄为：%d"%(self.name, self.age)

	def eat(self):
		print("%s is eating"%self.name)

	def drink(self):
		print("%s is drinking COCOkele"%self.name)


tom = Cat("汤姆", 40)    # 创建对象时自动调用
tom.eat()
tom.drink()
print(tom)   # 当使用函数 str 或使用函数 print 时被调用，显示信息为：汤姆的年龄为：40
print("")
lanmao = Cat("蓝猫", 18)   # 创建对象时自动调用
lanmao.eat()
lanmao.drink()
print(lanmao)		 # 当使用函数 str 或使用函数 print 时被调用  显示信息为：蓝猫的年龄为：18
