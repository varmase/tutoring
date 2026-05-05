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
        guess = ((right_index - left_index) // 2) + left_index
        print("left index: " + str(left_index))
        print("right index " + str(right_index))
        print(guess)
        #if nums[left_index] > guess:
            #print("xxxx")
        #else: 
            #if nums[right_index] < guess:
        if nums[guess] < target:
            left_index = guess + 1
        if nums[guess] > target:
            right_index = guess - 1
        if nums[guess] == target:
            return True
        if left_index > right_index:
            print(guess)
            return False
print(binary_search(nums, -17))

