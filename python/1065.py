"""
한수
"""
r = 0
for i in range(1, int(input())+1):
    if i < 100 or int(str(i)[2]) - int(str(i)[1]) == int(str(i)[1]) - int(str(i)[0]): r += 1
print(r)