n = int(input())
i = 1
while n > i:
    n -= i
    i += 1
print(f'{i-n+1}/{n}' if i % 2 else f'{n}/{i-n+1}')