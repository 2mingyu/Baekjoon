"""
하노이 탑 이동 순서
원판12345를 (1,3)으로 = 원판1234를 (1,2)로 + 원판5를 (1,3)으로 + 원판1234를 (2,3)으로
원판1234를 (1,3)으로 = 원판123을 (1,2)로 + 원판4를 (1,3)으로 + 원판123을 (2,3)으로
원판123을 (1,3)으로 = 원판12를 (1,2)로 + 원판3을 (1,3)으로 + 원판12를 (2,3)으로
원판12를 (1,3)으로 = 원판1을 (1,2)로 + 원판2를 (1,3)으로 + 원판1을 (2,3)으로

원판123을 (1,2)로 = 원판12를(2,3)으로 + 원판3을 (1,2)로 + 원판12를 (3,2)로
원판123을 (2,3)으로 = 원판12를 (2,1)로 + 원판3을 (2,3)으로 + 원판12를(1,3)으로
"""
def hanoi(n, A, B, C):
    r = ''
    if n == 1:
        r += str(A) + ' ' + str(B) + '\n'
    else:
        r += hanoi(n-1, A, C, B)
        r += str(A) + ' ' + str(B) + '\n'
        r += hanoi(n-1, C, B, A)
    return r
N = int(input())
result = hanoi(N, 1, 3, 2)
print(len(result) // 4)
print(result)