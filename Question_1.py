"""Move Zeroes
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]

Constraints:
a. 1 <= nums.length <= 10^4
b. -2^31 <= nums[i] <= 2^31 - 1"""
def moveZeros(nums):
    k = 0
    n=len(nums)
    for i in range(0,n):
        if nums[i]!=0:
            nums[k]=nums[i]
            k=k+1
    while k<n:
        nums[k]=0
        k = k+1

arr=[0,1,0,3,12]
print("Array before shifting zeroes")
print(arr)
moveZeros(arr)
print ("List after moving zeros ")
print(arr)