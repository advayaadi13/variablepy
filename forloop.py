for i in range(1,21):
    print(f"23 x {i} = {23 * i}")

for i in range(1,47):
    print(f"23 x {i} = {23 * i}")

n = int(input("Enter the number of rows: "))

for i in range(1, n+1):

    for j in range(i):
        print('*', end='')
    print()


