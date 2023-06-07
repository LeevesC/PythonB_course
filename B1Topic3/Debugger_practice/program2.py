# A program to add all even numbers between 0 and 20 (inclusive)
import pdb
sum = 0
x = 0
i = 20

while i>0:
    if i%2==0:
        sum += i
    i-=1
print(sum)