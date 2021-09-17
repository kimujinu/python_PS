
def dp(n):
    if n <= 2:
        return n - 1
    return min(dp(n//3) + n % 3 + 1, dp(n//2) + n % 2 + 1)

print(dp(int(input())))