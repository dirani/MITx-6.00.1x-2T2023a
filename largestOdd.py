"""
Write a program that examines three variables—x, y, and z—
and prints the largest odd number among them. If none of them are odd, it
should print a message to that effect.
"""

x = [None] * 33
for i in range(3):
    x[i] = int(input('Enter x: '))

largest = 0

for i in range(3):
    if x[i] > largest and x[i]%2 == 1:
        largest = x[i]

if largest == 0:
    print("None of them are odd")
else: 
    print("The largest odd number is: ", end='')
    print(largest)

