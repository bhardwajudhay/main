1 palindrome number
string=(input("enter the letter"))
if (string == string[::-1]):
    print(string,"is a palindrome number")
else:
    print(string,"is not a palindrome number")

num=int(input("enter number: "))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(temp==num):
    print("palin")
else:
    print("no")
