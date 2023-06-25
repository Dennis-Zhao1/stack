# How to implement the min() function when using stack with time complexity O(1)
nums = [1,3,2,4,-1]
nums1 = [1,-3,-5,6,9,-20,6]

def min_function(nums):
    stack1 = []
    stack2 = []
    min = nums[0]
    for item in nums:
        if item < min:
            min = item
        stack1.append(item)
        stack2.append(min)
    return stack2.pop()

min = min_function(nums1)
print(min)
