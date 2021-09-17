
def solution(n):

    answer = 0
    temp1 = format(n, 'b')
    oneCount = 0
    for i in str(temp1):
        if i == '1' :
            oneCount += 1

    while True:
        n+=1
        temp = n
        vsOneCount = 0
        temp2 = format(temp,'b')
        for i in str(temp2):
            if i == '1':
                vsOneCount += 1
        if vsOneCount == oneCount:
            answer = int(temp)
            return answer


print(solution(int(input())))