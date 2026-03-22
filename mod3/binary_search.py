#

nums = [1, 2, 3, 4, 5, 6, 7 , 8, 9, 10]

def practice(nums, target):
    for n in nums:
        #print(n)
        if n == target:
            return True
    return False
#O(n)
        

