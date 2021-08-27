n, k = map(int, input().split())
count = 0
while True:
    if(n != 1):
        if((n % k) != 0):
            if(n == 1):
                break
            n -= 1
            count += 1
        else:
            if(n == 1):
                break
            n //= k
            count += 1
    elif(n == 1):
        break

print(count)
