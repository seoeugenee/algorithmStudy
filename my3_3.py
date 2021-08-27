n, m = map(int, input().split())
result = 0

for i in range(n):
    #data = map(int , input().split())  #llist로 안해도 되는듯
    data = list(map(int , input().split()))  #이 코드가 답안에 나온 코드
    small = min(data)  #현재 줄에서 가장 작은 수 찾기
    result = max(result, small)  #가장 작은 수들 중에서 가장 큰 수 찾기

print(result)
#수정하다 보니 min() 함수를 이용하는 답안과 동일
