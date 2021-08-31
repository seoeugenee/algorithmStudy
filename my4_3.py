string = input()
row = int(string[1])
column = int(ord(string[0])) - int(ord('a')) + 1
result = 0
list = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

for i in range(8):
    r = row + list[i][0]  #이동한 위치는 새 변수에서 확인 row, column은 고정
    c = column + list[i][1]
    #if r < 1 or r > 8 or c < 1 or c > 8:  #가장 처음의 위치는 고정인데 잘못 생각
        #r -= list[i][0]
        #c -= list[i][1]
    #elif 1<= r <= 8 and 1<= c <= 8:
    if 1<= r <= 8 and 1<= c <= 8:
        result += 1
    
print(result)
