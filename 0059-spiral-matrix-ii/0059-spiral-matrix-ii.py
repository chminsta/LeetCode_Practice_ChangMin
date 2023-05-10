class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        #4
        #1  2  3   4
        #12 13 14  5
        #11 16 15  6
        #10  9  8  7
        #[1,2,3,4] [12,13,14,5] [11,16,15,6] [10,9,8,7]
        #[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
        
        #도저히 모르겠어서
        #https://leetcode.com/problems/spiral-matrix-ii/discuss/22290/Python-easy-to-follow-solution.
        #참고
        matrix = [[None] * n for _ in range(0, n)]

        top, bottom = 0, n - 1
        left, right = 0, n - 1

        numbers = (i for i in range(1, n ** 2 + 1))

        while left <= right and top <= bottom:

            for col in range(left, right + 1):
                matrix[top][col] = next(numbers)
            top += 1

            for row in range(top, bottom + 1):
                matrix[row][right] = next(numbers)
            right -= 1

            for col in range(right, left - 1, -1):
                matrix[bottom][col] = next(numbers)
            bottom -= 1

            for row in range(bottom, top - 1, -1):
                matrix[row][left] = next(numbers)
            left += 1

        return matrix      