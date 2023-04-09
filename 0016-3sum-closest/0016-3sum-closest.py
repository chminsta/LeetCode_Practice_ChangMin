class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums)==3:
            return sum(nums)
        nums.sort()
        
        #if target is small or big
        if sum(nums[:3]) > target:
            return sum(nums[:3])
        elif sum(nums[len(nums)-3:])<target:
            return sum(nums[len(nums)-3:])
        
        #make variable closest      
        closest = sum(nums[:3])
        
        #make two pointers to check faster
        for i in range(len(nums) - 2):
            j = i+1
            k = len(nums) - 1 
            while j < k:
                test = nums[i]+nums[j]+nums[k]
                if test == target:
                    return test
                
                if abs(test - target) < abs(closest - target): #check if its closer
                    #update closest
                    closest = test
                    
                if test < target:
                    #increasing test
                    j += 1
                elif test > target:
                    #decreasing test
                    k -= 1
            
        return closest
    
    
    
