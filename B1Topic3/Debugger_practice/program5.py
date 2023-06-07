# A program to add numbers until the user enters 0, then print the total

total = 0
current = -1
while (current!=0):
    current = int(input('Enter a number: '));
    total = total + current
print(total)

# Hint: What happens if a user types in something other than a number?