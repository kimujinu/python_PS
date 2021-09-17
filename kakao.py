from collections import deque
import sys

def bfs(x,y,room):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<5 and 0<=ny<5 :
                if room[nx][ny] == 'X':
                   continue
                if room[nx][ny] == 'P':
                    return 0
                else :
                    for j in range(4):
                        px = nx + dx[j]
                        py = ny + dy[j]
                        if 0 <= px < 5 and 0 <= py < 5 and (px != x or py != y):
                            if room[px][py] == 'P':
                                 return 0
    return 1

dx = [-1,1,0,0]
dy = [0,0,-1,1]

places = [
    ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
    ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
    ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
    ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
    ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]
]



def solution(places):
    answer = []
    for room in places:
        stop = False
        for x in range(5):
            for y in range(5):
                if room[x][y] == 'P':
                    if bfs(x, y, room) == 0:
                        stop = True
                        break
                if stop == True:
                    break
        if stop == True:
           answer.append(0)
        else:
           answer.append(1)

    return answer

solution(places)