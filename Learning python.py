Exp1 :print odd and even number between a range. ask user to enter lower and upper range
lower = int(input("Enter lower limit of range: "))
upper = int(input("Enter upper limit of range: "))
print("Odd And Even numbers in the given range are: ")
for i in range(lower,upper+1):
    print(i)


Exp 2: ask user to enter 1.even 2.odd which numbers user wants to see
lower = int(input("Enter lower limit of range: "))
upper = int(input("Enter upper limit of range: "))
ch=int(input("Enter 1 for printing even numbers and 2 for odd numbers"))
if ch==1:
    for i in range (lower,upper+1):
        if (i%2==0):
            print(i)
else:
    for i in range (lower,upper+1):
        if (i%2!=0):
            print(i)

Exp 3:Sum of first 15 natural numbers
print("Sum of first 15 students:")
sum=0
for i in range (1,16,1):
    sum=sum+i
print(sum)

Exp 4: 1 to 1000 print all armstrong numbers
for num in range(1,1001):
    order = len(str(num))
    sum=0
    temp = num
    while temp>0:
        digit = temp% 10 #rightmost
        sum+= digit ** order
        temp //=10

    if num==sum:
        print(num)  

Exp 5: using for loop to print fibonacci series for first 10 elements
first_no=0
print(first_no)#0,1,1,2,3,5,8,13
second_no=1 
print(second_no)
for i in range(1,9):
    next_no= first_no+second_no
    print(next_no)
    first_no=second_no
    second_no=next_no


