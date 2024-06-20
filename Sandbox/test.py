c = 10000
count = 0
for i in range(0,10000):
    print(f"{chr(c+i)} ", end='')
    count += 1
    if count == 100:
        print()
        count = 0

