#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-01 23:17:37
# @Author  : zengyw (1004324878@qq.com)
# @Link    : ${link}
# @Version : $Id$

"""
现有一个数据库记录文件（见附件0005_1.txt），保存了学生课程签到的数据库记录。 内容格式如下:

('2017-03-13 11:50:09', 271, 131),
('2017-03-14 10:52:19', 273, 131),
('2017-03-13 11:50:19', 271, 126),

每一行记录保存了学生的一次签到信息。
每一次签到信息的记录，分为三个部分，分别是签到时间、签到课程的id号、签到学生的id号

要求大家实现下面的函数。其中参数fileName为数据库记录文件路径， 输出结果是将数据库记录文件中的学生签到信息保存在一个字典对象中，并作为返回值返回。

def putInfoToDict(fileName):

要求返回的字典对象的格式是这样的:

key是各个学生的id号， value是该学生的签到信息

   其中value，里面保存着该学生所有签到的信息

   其中每个签到的信息是字典对象，有两个元素： key 是lessonid的 记录课程id，key是checkintime的 记录签到时间

比如，对于上面的示例中的3条记录，相应的返回结果如下：

{
    131: [
        {'lessonid': 271,'checkintime':'2017-03-13 11:50:09'},
        {'lessonid': 273,'checkintime':'2017-03-14 10:52:19'},
    ],
    126: [
        {'lessonid': 271,'checkintime':'2017-03-13 11:50:19'},
    ]    
}
# F:\\松勤\\作业\\0005_1.txt

"""

# checkintime = []
# lessionId = []
# studentId = []

def putInfoToDict(fileName):
	with open(fileName) as f:
		myDict = {}
		for line in f.readlines():
			
	 		checkintime, lessonid, studentid = line.split(',')[:3]
	 		checkintime = checkintime.split('(')[1].strip()      #签到时间进一步处理
	 		studentid = studentid.strip()
	 		studentid = int(studentid.split(')')[0].strip())      #学生学号id进一步处理	
		 	
		 	infoDict = {}   #定义一个字典，记录签到时间和课程id

		 	myDict[studentid] = []#给字典赋值
		 	infoDict['lessonid'] = int(lessonid)
		 	infoDict['checkintime'] = checkintime.strip('\'')
		 	
		 	for studentid in myDict:
		 		myDict[studentid].insert(0,infoDict)
		
		return myDict


if __name__ == '__main__':
	import pprint
	myPath = 'F:\\松勤\\作业\\0005_1.txt'
	pprint.pprint(putInfoToDict(myPath))
