"""
샤틀버스
"""
x, y = map(int, input().split())
print(y-x if x<y else x+y)