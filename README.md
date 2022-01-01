# 인공지능 수업과제
인공지능 수업 과제로 작성했던 코드로, 수업시간에 배운 방법을 이용하여 N-Queens Problem과 Q-Learning 문제를 해결하는 것을 목표로 한다.

- Assignment 1: N-Queens Problem
- Assignment 2: Q-Learning

## Assignment 1

### 요구 사항
* Breadth First Search, Hill Climbing, Constraint Satisfaction Problems 알고리즘을 각각 이용하여 N-Queens Problem의 Solution을 찾는다.
* 임의의 N에 대하여, 1~N의 열(Column) 중 각 퀸의 행(row)위치를 출력하며, Solution이 존재하지 않을 경우 No Solution을 출력하도록 한다.

## Assignment 2
* Q-table을 기반으로 한 Q-learning을 구현한다.
* 맵에는 출발지점, 보너스장소, 폭탄, 목표지점이 있으며 폭탄에 부딪히지 않고 목표지점에 도달하는 것을 목적으로 한다.
* 여러 번 반복하여 출발지점부터 목표지점까지의 경로와 출발지점에서의 최대 Q(s,a)를 출력하도록 한다.
  * 폭탄 reward: -100
  * 목표지점 reward: 100
  * 보너스 지점 reward: 1, 10, 20 (각각에 대하여 결과 확인)
  * $\gamma$: 0.9