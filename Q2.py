binary_number = input("Enter the binary number :")

decimal_number = 0
power = 0

for digit in binary_number[::-1]:
    decimal_number += int(digit) * (2 ** power)
    power += 1

print(decimal_number)
