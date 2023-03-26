class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        i=0
        output=[]
        for num in nums:
            m = target - num
            try:
                ii=nums.index(m)
            except:
                i+=1
            else:
                if i!=ii:
                    output.extend([i,ii])
                    break
                else:
                    i+=1              
        return output