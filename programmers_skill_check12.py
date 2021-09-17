def solution(bridge_length, weight, truck_weights):
    time = 0
    q = [0] * bridge_length

    while q:
        time += 1
        q.pop(0)
        if truck_weights:
            if sum(q) + truck_weights[0] <= weight: # 다리에 들어갈수있는 조건
                q.append(truck_weights.pop(0))
            else: #빈공간 넣기
                q.append(0)

    return time

print(solution(2,10,[7,4,5,6]))