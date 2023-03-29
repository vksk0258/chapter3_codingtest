# 교점에 별 만들기 p.63\

# 1.주어진 직선에서 교점을 구한다
for i in range(n): # 주어진 직선의 방정식 개수만큼 for 문을 돌린다.
    a, b, e = line[i]
    for j in range(i + 1, n):
        c, d, f = line[j]
        if a * d == b * c: continue # ad - bc = 0인 경우 평행이다
        x = (b * f - e * d) / (a * d - b * c) 
        y = (e * c - a * f) / (a * d - b * c)
        
# 2.그중 정수 교점만 따로 변수로 저장한다.
if x == int(x) and y == int(y):
    x = int(x)
    y = int(y)
    pos.append([x,y])