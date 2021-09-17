from collections import deque

def solution(progresses, speeds):
    output = deque()
    answer = []
    for p,s in zip(progresses,speeds):
        day = 1
        while True:
            if p + s >= 100:
                output.append(day)
                break
            else:
                p = p + s
                day += 1

    while output:
        temp = output.popleft()
        count = 1
        while output and temp >= output[0]:
            output.popleft()
            count += 1
        answer.append(count)
    return answer

print(solution([95, 90, 99, 99, 80, 99]	,[1, 1, 1, 1, 1, 1]))