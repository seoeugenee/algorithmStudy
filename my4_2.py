h = int(input())
string = str(h) + '59' + '59'
num = int(string) + 1
count = 0
for i in range(num):  #이렇게 하면 60분 60초 이상까지 계산하므로 안된다!
    if '3' in str(i):
        count += 1

print(count)  #잘못된 결과값 나온다
