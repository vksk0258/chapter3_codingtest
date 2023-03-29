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
    
# 3.교점을 모두 표현할 수 있는 최소한의 사각형을 알아낸다.
if x_min > x: x_min = x
if y_min > y: y_min = y
if x_max < x: x_max = x
if y_max < y: y_max = y

# 4.모든 교점을 *로 찍어서 표현한다.
x_len = x_max - x_min + 1
y_len = y_max - y_min + 1
coord = [["."] * x_len for _ in range(y_len)] # for문에서 _사용은 range()의 횟수만큼돌 반복된다는 뜻 변수를 사용안함

for star_x, star_y in pos:
    nx = star_x + abs(x_min) if x_min < 0 else star_x - x_min # x,y좌표는 음수 값이 존재하므로 음수일 경우 절댓값을 더해준다
    ny = star_y + abs(y_min) if y_min < 0 else star_y - y_min
    coord[ny][nx] = '*' # 별의 좌표를 찍는다