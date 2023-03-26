class Solution:
    def romanToInt(self, s: str) -> int:
        nums = list(s)
        i=0
        for num in nums:            
            if num == "M":
                nums[i]=1000
            elif num == "D":
                nums[i]=500
            elif num == "C":
                nums[i]=100
            elif num == "L":
                nums[i]=50  
            elif num == "X":
                nums[i]=10
            elif num == "V":
                nums[i]=5
            elif num == "I":
                nums[i]=1
            i+=1
        i=0
        while i<len(nums)-1:
            if nums[i] < nums[i+1]:
                nums[i]=nums[i+1]-nums[i]
                nums[i+1]=0
                i+=2
            else:
                i+=1
        return sum(nums)