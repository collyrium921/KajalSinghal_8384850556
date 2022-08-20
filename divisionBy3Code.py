#get the number of sequences
def checkSequence(num):
    quotient = num//3
    remainder = num%3
    if(remainder!=0):
        return quotient*2+remainder-1
    else:
        return quotient*2

#take input of both numbers
num1 = int(input('Enter first number')) 
num2 = int(input('Enter second number')) 

#subtract the number of sequences of num1 from num2 to prevent adding duplicate sequence
result = checkSequence(num2)-checkSequence(num1-1)
print(result)