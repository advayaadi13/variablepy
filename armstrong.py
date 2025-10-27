num = int(input("Enter a number: "))
n = len(str(num))
sum_of_powers = sum(int(d) ** n for d in str(num))
if num == sum_of_powers:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
