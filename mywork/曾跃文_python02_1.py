with open(r'C:\Users\zyw20180716\Desktop\log.txt', 'r') as f:
    sum_jpeg = 0
    sum_jpg = 0
    sum_png = 0
    sum_json = 0
    for line in f.readlines():   #循环获取文件中的每一行
        line_list = line.split('\t')    #通过split('\t')将文件分割
        line_list = line_list[0:2]      #列表是可变元素，通过切片赋值，取原列表第0和第1行作为列表的值

        if line_list[0].endswith('.jpeg'):
            sum_jpeg += int(line_list[1])
        #通过endwith('.jpeg')判断列表第一个元素是否以'.jpeg'结尾，如果是，则将列表的第2个元素，\
        #即line_list[1]，转为整形，int(line_list[1]), 然后通过'+='的方式，赋值给sum_jpeg,下面几个与此类似

         
        if line_list[0].endswith('.jpg'):
            sum_jpg += int(line_list[1])

        if line_list[0].endswith('.png'):
            sum_png += int(line_list[1])

        if line_list[0].endswith('.json'):
            sum_json += int(line_list[1])

    print('jpeg  ', sum_jpeg)
    print('jpg  ', sum_jpg)
    print('json  ', sum_json)
    print('png  ', sum_png)
