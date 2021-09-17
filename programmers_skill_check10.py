def solution(array, commands):
    answer = []
    for i in commands:
        temp = []
        for j in range(i[0]-1,i[1]):
            temp.append(array[j])
        temp.sort()
        answer.append(temp[i[2]-1])

    return answer

print(solution([1,5,2,6,3,7,4],[[2,5,3],[4,4,1],[1,7,3]]))