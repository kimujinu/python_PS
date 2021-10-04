N = int(input())
array = list(map(int,input().split()))
result = 0
temp_sum = 0
def backtracking(sum):
    global result,temp_sum
    if len(array) == 2:
        result = max(result,sum)
        return
    else:
        for i in range(1,len(array)-1):
            temp_sum = array[i-1]*array[i+1]
            temp2 = array[i]
            del array[i]
            backtracking(sum+temp_sum)
            array.insert(i,temp2)

backtracking(0)
print(result)