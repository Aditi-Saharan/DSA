Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ele = None #majority element
        c=0 #count of majority element
        for i in nums:
            if c == 0:    #count is zero , assign the element to majority element
                ele = i
            c += (1 if i == ele else -1)   #increment the count if the the current majority element and element in list is same else -1
        return ele
