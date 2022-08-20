#get the input of the number
num = int(input("Enter a number"))
#assign the number to a temporary varaible
temp = num
reverse_num =0;
#reverse the digits of the number
while temp>0:
    digit = temp%10
    reverse_num = reverse_num*10+digit
    temp=temp//10
if(num == reverse_num):
     print('Yes')
else:
    print('No')     