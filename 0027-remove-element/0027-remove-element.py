class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        try:
            while val in nums:
                nums.remove(val)
        except:
            k = len(nums)
            return k
        finally:
            k = len(nums)
            return k

        