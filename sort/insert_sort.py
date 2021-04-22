# coding=utf-8

# 插入排序

def sort(list):
    for i in range(1, len(list)):
        value = list[i]  # 插入值

        j = i - 1  # 记录插入位置  j+1 代表插入的位置
        while j >= 0:  # 不用 for 循环是因为 j 为 -1 的情况
            if list[j] > value:
                list[j + 1] = list[j]
            else:
                break
            j -= 1

        list[j + 1] = value
    return list


# 变种--希尔排序
def shell_sort(list):
    n = len(list)
    gap = int(n / 2)

    while gap > 0:

        for i in range(gap, n):

            temp = list[i]
            j = i
            while j >= gap and list[j - gap] > temp:
                list[j] = list[j - gap]
                j -= gap
            list[j] = temp
        gap = int(gap / 2)

    return list


if __name__ == '__main__':
    arr = [9, 6, 2, 5, 1, 8, 3, 4, 7]
    shell_sort(arr)
    for i in arr:
        print i
