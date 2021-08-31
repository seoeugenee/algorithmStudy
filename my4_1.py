n=int(input())
x = 1
y = 1
plans=list(input().split())

for p in plans:
    if p =='R':
        y += 1
        if (x<1 or x>n or y<1 or y>n):
            y -= 1
            
    elif p=='L':
        y -= 1
        if (x<1 or x>n or y<1 or y>n):
            y += 1
            
    elif p=='U':
        x -= 1
        if (x<1 or x>n or y<1 or y>n):
            x += 1

    elif p=='D':
        x += 1
        if (x<1 or x>n or y<1 or y>n):
            x -= 1

print(x, y)
