# Hanoi
# 汉诺塔
# A             B               C
# souce     middle      target

count  = 0

def hanoi(n, source, target, middle):
    global count
    if n ==1:
        print('{}: {} -> {}'.format(n, source, target))
    else:
        hanoi(n - 1, source, middle, target) # 把 n -1 个圆盘从A搬到B
        print('{}: {} -> {}'.format(n, source, target))
        hanoi(n - 1, middle, target, source) # 把 n -1 个圆盘从B搬到C
    count +=1


def main():
    hanoi(3, 'A','C','B')
    print(count)


main()
