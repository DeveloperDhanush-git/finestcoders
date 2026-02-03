def coinChange(coins,change):
   n=len(coins)
   dp=[[float('inf')]*(change+1) for _ in range(n+1)]
   for i in range(n+1):
       dp[i][0]=0
   for i in range(1,n+1):
       for j in range(1,change+1):
           if j<coins[i-1]:
               dp[i][j] = dp[i-1][j]
           else:
               dp[i][j] = min(dp[i-1][j],1+dp[i][j-coins[i-1]])
   for i in range(1,n+1):
       for j in range(1,change+1):
           print(dp[i][j],end=" ")
       print()
   return dp[n][change]
coins=[1,5,6,9]
change=11
result=coinChange(coins,change)
print(result)


