#left index: changes when guess is lower
#right index: changes when guess is higher

nums = [1, 2, 3, 4, 5, 6, 7 , 8, 9, 10, 11, 12, 13, 14, 15]

def practice(nums, target):
    for n in nums:
        #print(n)
        if n == target:
            return True
    return False
#O(n)
        
def binary_search(nums, target):
    left_index = 0
    right_index = len(nums) - 1
    while True:
        guess = (nums[left_index] + nums[right_index]) // 2
        print("left index: " + str(left_index))
        print("right index " + str(right_index))
        print(guess)
        if guess < target:
            left_index = guess + 1
        if guess > target:
            right_index = guess - 1
        if guess == target:
            return True
        
binary_search(nums, 10)


