from queue import deque
from copy import deepcopy
import random

def checkConflict(arr): # Queen이 조건에 맞는지 여부 리턴
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]: # 같은 행에 존재
                return False
            elif abs(arr[i] - arr[j]) == abs(i-j): # 대각선 상에 위치
                return False

    return True

def checkConflictNum(arr): # Queen끼리 conflict되는 개수 리턴
    result = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]: # 같은 행에 존재
                result += 1
            elif abs(arr[i] - arr[j]) == abs(i-j): # 대각선 상에 위치
                result += 1

    return result

def bfs(N):
    # 큐에 넣기전 지금까지 놓은 상태에서 충돌이 일어난다면 더 탐색하지 않고 백트래킹 해서 BFS탐색을 한다면 더 좋은 결과가 나올 것이나,
    # csp에서 백트래킹을 사용할 것이므로 성능 비교를 위해 일부러 모든 state를 다 탐색하는 식으로 하였다.

    bfsQueue = deque() # (각 열에 있는 Queen이 위치한 행번호들의 배열, 총 놓인 Queen 수)의 튜플들이 담김
    bfsQueue.append(([], 0))

    while bfsQueue:
        tempArr, tempNum = bfsQueue.popleft()
        if tempNum == N: # N개의 퀸들이 조건에 다 맞게 배치된 경우 solution 발견
            if checkConflict(tempArr):
                return tempArr
        else:
            for i in range(1, N+1):
                bfsQueue.append((tempArr+[i], tempNum+1)) # 큐에 넣는 원소는 모두 다르므로 굳이 방문여부를 체크할 필요가 없다.

    return None

def hc(N):
    for i in range(100): # 총 100회 random restart
        tempArr = [random.randrange(1, N+1) for i in range(N)]

        while True:
            startConflict = checkConflictNum(tempArr) # 처음 conflict 수
            minConflict = startConflict # 하나 움직였을 때 나올 수 있는 conflict 최솟값
            tempMinArr = tempArr[:] # conflict 최솟값이 나오는 그 때의 Queen 배치

            if startConflict == 0: # 해를 찾은 경우
                return tempArr

            for j in range(N): # 한 칸씩 움직이는 경우 중 최소 conflict가 되는 경우를 찾음
                for j2 in range(1, N+1):
                    if j2 == tempArr[j]:
                        continue

                    tempNewArr = tempArr[:]
                    tempNewArr[j] = j2
                    newConflict = checkConflictNum(tempNewArr)

                    if minConflict > newConflict:
                        minConflict = newConflict
                        tempMinArr = tempNewArr[:]

            if minConflict == startConflict: # 더 이상 conflict 수를 줄일 수 없다면 해가 없거나 local minimum에 빠진 것임
                break
            else:
                tempArr = tempMinArr
    
    return None
                    
def cspFindCase(legalPositionArr, currentArr, N, num): # Queen이 num개 놓인 상태에서 num+1번째 Queen을 놓는 방법을 탐색
    if N == num:
        return currentArr
    
    for e in [i for i in range(N) if legalPositionArr[num][i]]: # num+1번째 Queen을 놓일 수 있는 행번호는 legalPositionArr[num]에 존재한다
        tempPositionArr = deepcopy(legalPositionArr)
        for j in range(num+1, N):
            tempPositionArr[j][e] = False # 같은 행에 놓일 수 없음
            if e+(j-num) < N:
                tempPositionArr[j][e+(j-num)] = False # (오른쪽 아래)대각 방향에 놓일 수 없음
            if e-(j-num) >= 0:
                tempPositionArr[j][e-(j-num)] = False # (오른쪽 위)대각 방향에 놓일 수 없음

        result = cspFindCase(tempPositionArr, currentArr+[e+1], N, num+1) # num+1번째 Queen을 놓고 새로운 곳을 탐색한다. (currentArr에 놓을 때 1행부터 시작하도록 1을 더함)
        if result != None:
            return result

    return None # 놓을 수 있는 곳이 empty value set일 경우 여기에 도달한다
    

def csp(N):
    # forward checking을 이용함
    legalPositionArr = [[True for _ in range(N)] for _ in range(N)] # legalPos[a][b]는 a+1번째 Queen이 b+1번행에 위치하는게 가능한지 표시한다.
    return cspFindCase(legalPositionArr, [], N, 0);

def main():
    with open("input.txt", "r") as inputFile:
        inputLines = inputFile.readlines()
        for inputLine in inputLines:
            N, functionChoice = inputLine.rstrip().split()
            N = int(N)
            solution = None

            if functionChoice == "bfs":
                solution = bfs(N)
            elif functionChoice == "hc":
                solution = hc(N)
            elif functionChoice == "csp":
                solution = csp(N)

            if solution == None:
                with open(str(N) + "_" + functionChoice + "_output.txt", "w") as outputFile:
                    outputFile.write("no solution")
            else:
                with open(str(N) + "_" + functionChoice + "_output.txt", "w") as outputFile:
                    for i in range(len(solution)):
                        outputFile.write(str(solution[i]))
                        if i != (len(solution) - 1):
                            outputFile.write(" ")
    

if __name__ == "__main__":
    main()