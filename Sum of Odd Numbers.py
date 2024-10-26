n = int(input("Enter an integer: "))

sum = ""
total = 0

for i in range(1, n, 2):
    sum += str(i) + " "
    total += i

print(f"The sum of the numbers: {sum}is {total}")