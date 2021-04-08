# coding=utf-8

# 冒泡排序

def sort(list):
    # 执行轮次数
    num = 0
    size = len(list)
    for x in range(size):
        num += 1
        for y in range(size - x - 1):
            if list[y] > list[y + 1]:
                list[y],list[y+1] = list[y+1],list[y]

    print '执行轮次数：' + str(num)


# 优化冒泡排序
def optimization_sort(list):
    # 执行轮次数
    num = 0
    size = len(list)
    flag = True
    for x in range(size):
        num += 1
        # 上一轮还有替换，这一轮还需要比较
        if flag:
            flag = False

            for y in range(size - x - 1):
                if list[y] > list[y + 1]:
                    list[y], list[y + 1] = list[y + 1], list[y]
                    # 上一轮有过替换，下一次还需要比较
                    flag = True
        # 上一轮没有替换，不需要再比较了
        else:
            print '执行轮次数：' + str(num)
            return

    print '执行轮次数：' + str(num)

if __name__ == '__main__':
    arr = [9,6,2,5,1,8,3,4,7]
    sort(arr)
    for i in arr:
        print i

