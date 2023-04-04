class Solution:
    def climbStairs(self, n: int) -> int:
        #점화식을 생각하자. n개의 계단의 마지막은 1또는 2인데 
        #그 두가지를 생각하면 n-2계단의 경우+n-1계단의경우와 같다 
        dp = [0] * (n+1)
        dp[0], dp[1] = 1, 1

        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]

        