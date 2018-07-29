students_msg = input ('pls enter student\'s person message:\n')

sub_students_msg = students_msg.split(';')
#得到一个列表
sub_students_msg.pop()
#去掉分割后，最后的空或者空格元素，
t_students_msg = tuple(sub_students_msg)
#并且将列表转换为元组t_students_msg

for i in range(len(t_students_msg)):
    student_msg = t_students_msg[i].split(',')
	#将得到的第i个元素，用逗号分割后，得到的列表，转换为元组student_msg
    student_msg[0] = student_msg[0].strip()
    student_msg[1] = int(student_msg[1].strip())
	#去掉元素前后空格
    t_student_msg = tuple(student_msg)
	#将去掉元素前后空格后，得到的列表，转换为元组student_msg

    print('{0[0]:20s}:  {0[1]:02d}'.format(t_student_msg))
	#输出目标数据
	

