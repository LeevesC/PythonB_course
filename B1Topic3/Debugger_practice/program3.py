# A program print the multiplication tables
# output should be:
# 1 2 3 4 5 6 7 8 9 10
# 2 4 6 8 10 12 14 16 18 20
# 3 6 9 12 15 18 21 24 27 30
# ...
# 10 20 30 40 50 60 70 80 90 100


total = 0
i = 1
while i<=10:
    j = 1
    while j<=10:
        print(i*j , end =" " )
        j+=1
    i+=1
    print()