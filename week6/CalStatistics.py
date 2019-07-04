# CalStatistics.py
import random

# 返回长度为size的list， 值在0, 99之间
def getNum(size):
    nums = []
    for i in range(size):
        nums.append(random.randint(0, 99))
    return nums

# 获取list 平均值
def getAvg(nums):
    size = len(nums)
    if size <= 0:
        return 0.0
    avg = 0.0
    '''
    for i in range(size):
        avg += nums[i]
    '''
    for num in nums:
        avg += num
    else:
        return avg / size


# 获取方差
def getVariance(nums):
    avg = getAvg(nums)
    if avg ==0:
        return avg
    
    sum = 0.0 # ( avg - nums[0] ) ^2 +... + (avg - nums[i] ) ^ 2
    variance = 0.0 # sum / len(nums)  方差

    for num in nums:
        sum += (avg - num) ** 2
    else:
        return (sum / len(nums)) ** 0.5

# 获取中位数
def getMid(nums):
    sorted(nums)
    size = len(nums)
    if size == 0:
        return size
    
    if (size % 2) == 0:
        # size = 4,   index : 0, 1, 2, 3
        return (nums[size // 2] + nums[(size // 2) -1]) / 2
    else:
        return nums[size // 2]
    
def main():
    nums = getNum(6)
    print(nums)

    print(getAvg(nums))
    print(getVariance(nums))
    print(getMid(nums))


main()

                
        
