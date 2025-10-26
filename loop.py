#find sum and average of numbers
Total = 0
for i in range(1 ,6):
   num = int(input("Enter number " + str(i) + ":"))
Total += num
average =Total/5
print("the sum is:", Total)
print("the average is:", average)

#print number until user enter 0
num = int(input("enter a number: "))
while num != 0:
    print("you entered: ", num)
    num = int(input("Enter a number: "))
    print("loop ended")
#print star pattern
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
        print()