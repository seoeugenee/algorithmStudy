n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
one = data[n-1]
two = data[n-2]

result = 0

#for i in range(m):  #제일 처음 적은 코드 횟수-총 횟수가 m번이라 적었지만 잘못된 생각
while True:
    #if m != 0: #겉에서는 0인지 확인할 필요가 없네....
        for i in range(k):
            if(m == 0):  #새로 더하기 전에 0인지 확인하는 과정 필수
                break
            result += one
            m -= 1
        if(m == 0):
            break
        result += two
        m -= 1
        
    #elif(m == 0):
        #break

print(result)
#결과값이 잘 나오도록 수정하다보니 책의 단순하게 푸는 답안과 같은 코드가 되었다
