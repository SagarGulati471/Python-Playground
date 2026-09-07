def fib(n, dp):
  if n == 0 or n == 1:
    return n

  if dp[n]:
    return dp[n]
  fibonnaci = fib(n - 1, dp) + fib(n - 2, dp)
  dp[n] = fibonnaci
  return fibonnaci

# Time - O(N)
# Space - O(N)





# Time - O(n)
# Solution with O(1) Space
def fib2(n):
  if n <= 1:
    return 1
    

  prev2 = 0
  prev1 = 1
  for i in range(2, n+1):
    print(i, prev1, prev2)
    current = prev1 + prev2
    prev2 = prev1
    prev1 = current
  return prev1





n = int(input("Enter the number"))
dp = [0] * (n+1)
print(fib(n, dp))
print(fib2(n))


