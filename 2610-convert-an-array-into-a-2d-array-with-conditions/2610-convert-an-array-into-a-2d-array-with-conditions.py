class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        result = []

        for num in nums:
            added = 0
            for row in result:
                if num not in row:
                    row.append(num)
                    added = 1
                    break
            if not added:
                result.append([num])
        return result