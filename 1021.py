import sys

N,M = 10,3#map(int,sys.stdin.readline().split())
data_list = [i for i in range(1,N+1)]
arraylist = [2,9,5]#list(map(int,sys.stdin.readline().split()))
temp = 0
for i in arraylist :
    k = data_list.index(i)
    temp += min(k,len(data_list)-k)
    data_list = data_list[k+1:]+data_list[:k]
print(temp)
