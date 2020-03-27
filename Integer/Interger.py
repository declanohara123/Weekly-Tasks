# file where if you input a number, the program halves it if it is even, but tripples itand adds one if the number is odd

a = int(input("Please enter a positive integer: "))
b = int (2)

print (a , end=' ')


while a > 1:

    if a % b == 0:
        a /= 2
        print (a, end=' ')  

    else:
        a = (a * 3) + 1
        print (a, end=' ')

print ("Thank you")
