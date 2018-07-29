"""
现有文件1（如下，请保存到文件file1.txt中）， 记录了公司员工的薪资，其内容格式如下

name: Jack   ;    salary:  12000
 name :Mike ; salary:  12300
name: Luk ;   salary:  10030
  name :Tim ;  salary:   9000
name: John ;    salary:  12000
name: Lisa ;    salary:   11000

每个员工一行，记录了员工的姓名和薪资，
每行记录 原始文件中并不对齐，中间有或多或少的空格

现要求实现一个python程序，计算出所有员工的税后工资（薪资的90%）和扣税明细，
以如下格式存入新的文件 file2.txt中，如下所示

name: Jack   ;    salary:  12000 ;  tax: 1200 ; income:  10800
name: Mike   ;    salary:  12300 ;  tax: 1230 ; income:  11070
name: Luk    ;    salary:  10030 ;  tax: 1003 ; income:   9027
name: Tim    ;    salary:   9000 ;  tax:  900 ; income:   8100
name: John   ;    salary:  12000 ;  tax: 1200 ; income:  10800
name: Lisa   ;    salary:  11000 ;  tax: 1100 ; income:   9900

要求像上面一样的对齐
tax 表示扣税金额和 income表示实际收入。注意扣税金额和 实际收入要取整数  

分析：
1 制作文件file.txt，暂时放在桌面
2 打开文件，并用f.readlines() 获取文件中各行元素
3 数据格式调整 以及数据计算
"""


with open(r'C:\Users\zyw20180716\Desktop\file.txt') as f,open(r'C:\Users\zyw20180716\Desktop\file2.txt','w') as f2:
    for line in f.readlines():
        nameMsg, salaryMsg = line.split(';')   #对分割的元素进行加工处理
        nameMsg = nameMsg.strip()        #去掉名字部分前后的空格
        salaryMsg = salaryMsg.strip()    #去掉薪水部分前后的空格

        name_msg = nameMsg.split(':')     # 对名字部分进一步优化

        for i in range(0,len(name_msg)):
            name_msg[i] = name_msg[i].strip()              #去掉名字部分前后的空格
		

            salary_msg = salaryMsg.split(':') #对薪水部分进一步优化 

        for j in range(0,len(salary_msg)):
            salary_msg[j] = salary_msg[j].strip()          #去掉薪水部分前后的空格		
		
            income = int(int(salary_msg[1])*0.9)    #计算薪水
            tax = int(salary_msg[1]) - income       #计算税费

        standardOutPut = '{0[0]:s}:{0[1]:10s}  ;  {1[0]:s}:{1[1]:10s}  ; tax:{2:6d} ； income:{3:8d}'.format(name_msg,salary_msg,tax,income)
		# print(standardOutPut)
		#格式化输出
        f2.write(standardOutPut+'\n')	#将标准输出写入文件file2.txt	
