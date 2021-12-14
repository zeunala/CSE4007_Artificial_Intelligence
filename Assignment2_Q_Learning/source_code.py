
'''
수업에서는 Q-Learning 예시에서 S1~S6으로 나누고 table을 S1,a12 식으로 저장했으나,
여기서는 0번~24번 구역으로 나누고 table을 qTable[a][b] 식으로 저장함 (a번에 있는 상태에서 b번으로 갈 경우)
'''
import random

def main():
    with open("input.txt", "r") as inputFile:
        inputLines = inputFile.readlines()
        inputArr = []
        mapArr = [] # 2차원 배열 inputArr을 1차원 배열로 나타낸 것
        MAP_SIZE = 5 # 5*5 크기 기준
        qTable = [{} for _ in range(MAP_SIZE * MAP_SIZE)]
        
        BOMB_REWARD = -100
        GOAL_REWARD = 100
        BONUS_REWARD = 1
        gamma = 0.9
        
        startPos = 0
        goalPos = 24
        
        for inputLine in inputLines:
            inputArr.append(list(inputLine.rstrip()))
            
        for i in range(MAP_SIZE):
            for j in range(MAP_SIZE):
                if inputArr[i][j] == "S":
                    startPos = i * MAP_SIZE + j
                elif inputArr[i][j] == "G":
                    goalPos = i * MAP_SIZE + j
                mapArr.append(inputArr[i][j])
        
        # qTable 초기화
        for i in range(MAP_SIZE):
            for j in range(MAP_SIZE):
                mapNumber = i * MAP_SIZE + j # 5*5기준 0번~24번
                
                if mapNumber == goalPos: # goal 번호에 대한 QTable은 만들지 않음 (도착하면 끝이므로)
                    continue
                
                if i - 1 >= 0:
                    qTable[mapNumber][(i - 1) * MAP_SIZE + j] = 0
                if j - 1 >= 0:
                    qTable[mapNumber][i * MAP_SIZE + (j - 1)] = 0
                if i + 1 < MAP_SIZE:
                    qTable[mapNumber][(i + 1) * MAP_SIZE + j] = 0
                if j + 1 < MAP_SIZE:
                    qTable[mapNumber][i * MAP_SIZE + (j + 1)] = 0
        
        NUMBER_OF_REPETITIONS = 200 # 총 Learning할 횟수
        
        for i in range(NUMBER_OF_REPETITIONS):
            currentPos = startPos
            
            while currentPos != goalPos:
                # qTable[currentPos].keys()는 현재 위치에서 갈 수 있는 곳을 나타낸다.
                nextPos = random.choice(list(qTable[currentPos].keys()))
                immediateReward = 0
                if mapArr[nextPos] == "G":
                    immediateReward = GOAL_REWARD
                elif mapArr[nextPos] == "T":
                    immediateReward = BONUS_REWARD
                elif mapArr[nextPos] == "B":
                    immediateReward = BOMB_REWARD
                
                if nextPos == goalPos:
                    qTable[currentPos][nextPos] = immediateReward
                else:
                    qTable[currentPos][nextPos] = immediateReward + (gamma * max(qTable[nextPos].values()))
                
                currentPos = nextPos

        with open("output.txt", "w") as outputFile:
            currentPos = startPos
            while currentPos != goalPos:
                outputFile.write(str(currentPos) + " ")
                # qTable이 최대가 되는 key값 중 무작위로 선정
                currentPos = random.choice([k for k, v in qTable[currentPos].items() if max(qTable[currentPos].values()) == v])
            outputFile.write(str(currentPos) + "\n")
            
            outputFile.write(str(max(qTable[startPos].values()))) # 시작지점 Q함수 최댓값

if __name__ == "__main__":
    main()