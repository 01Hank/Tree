# coding=utf-8

# 选择排序

def sort(list):
    size = len(list)
    for i in range(size):
        min = i
        for j in range(i + 1, size):
            if list[j] < list[min]:
                min = j

        if min != i:
            # 交换
            list[i], list[min] = list[min], list[i]

    return list


if __name__ == '__main__':
    arr = [9, 6, 2, 5, 1, 8, 3, 4, 7]
    sort(arr)
    for i in arr:
        print i
