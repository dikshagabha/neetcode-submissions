class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = {}
        def dfs(i):
            ticketDays= [1, 7, 30]
            if i == len(days):
                return 0
            if i in dp:
                return dp[i]
            dp[i] = float('inf')
            j = i
            for numbers in range(len(ticketDays)):
                while j<len(days) and days[j]<days[i]+ticketDays[numbers]:
                    j+=1
                dp[i] = min(dp[i], costs[numbers]+dfs(j))

            return dp[i]
        return dfs(0)
                    