"""
请定义一个函数 mySort，参数为一个列表，参数列表中的元素都是整数.
mySort 函数需要将参数列表中的元素按从小到大排序，最终返回一个新的list。

请按下面算法的思路实现函数：

1. 创建一个新的列表newList
2. 先找出所有元素中最小的，append在newList里面
3. 再找出剩余的所有元素中最小的，append在newList里面
4. 依次类推，直到所有的元素都放到newList里面    

"""

newList = []
def mySort(inList):
    #for i in range(len(alist)):
        #number = min(alist)
        #newList.append(number)
        #alist.remove(min(alist))
    while len(inList) > 0:

        minNum = inList[0]
        minIdx = 0
        indx = 0 

        for num in inList:
            if minNum > num:
                minNum = num
                minIdx = indx
            indx += 1
        inList.pop(minIdx)
        newList.append(minNum)

    return newList


if __name__ == '__main__':
    l1 = [5,2,8,6,4,3,13]
    print(mySort(l1))
