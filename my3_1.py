n = 1260
count = 0

money = [500, 100, 50, 10]
for m in money:
    count += n // m
    n %= m

print(count)
