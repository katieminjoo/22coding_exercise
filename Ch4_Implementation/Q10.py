# 자물쇠와 열쇠
# 열쇠를 적당히 회전하고 이동시켜 자물쇠의 홈에 딱 맞게 끼우넣는것
# (0은 홈부분, 1은 돌기, 열쇠의 1과 자물쇠의 0, 자물쇠의 0과 열쇠의 1이 딱 맞으면됨.)
# 파이썬 > 1초에 2000만 ~ 1억 연산 처리 가능
# 완전탐색 시도 (다해보자)

key2 = [[0,0,0],[1,0,0],[0,1,1]]
lock2 = [[1,1,1],[1,1,0],[1,0,1]]
# result = True

# key의 돌기가 다른데로 새도, lock의 홈에만 맞으면됨.
# LOCK의 0부분을 key의 1로 어떻게 채울것인지. (남는 1은 밖으로 나가도 상관없음)

# 3*3 행렬이기 때문에 자물쇠 리스트의 크기를 3배 이상으로 변경 . (9*9) 자물쇠를 가운데두고 주위를 전부 0으로
# 왼쪽 위부터 시작해서 한칸씩 이동하며 열쇠를 더하고 자물쇠의 행렬이 전부 1인지 확인한다. (열쇠를 90도씩 돌려가며 4번 진행)

######
# 2차원 리스트 90도 회전 (그냥 외우는것이 나을듯)
answer = True
def rotate_a_matrix_by_90_degree(a):
    n = len(a) # 행 길이 계산
    m = len(a[0]) # 열 길이 계산
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-1-1] = a[i][j]
    return result


# 확장된 자물쇠의 중간부분이 모두 1인지 확인
def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length*2):
        for j in range(lock_length, lock_length*2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key,lock):
    n = len(lock)
    m = len(key)
    # 자물쇠의 크기를 기존 3배로 변환
    new_lock = [[0] * (n*3) for _ in range(n*3)]
    # 새로운 자물쇠의 중앙 부분에 기존의 자물쇠 넣기
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]

    # 4가지 방향에 대해 처리
    for rotation in range(4):
        key = rotate_a_matrix_by_90_degree(key) # 열쇠회전
        for x in range(n*2):
            for y in range(n*2):
                # 자물쇠에 열쇠를 끼워 넣기 ( 더해보기 )
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                # 새로운 자물쇠에 열쇠가 정확히 들어맞는지 검사
                if check(new_lock) == True:
                    return True
                # 자물쇠에서 열쇠를 다시 빼기 ( 숫자를 빼기 )
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]
    return False

print(solution(key2,lock2))