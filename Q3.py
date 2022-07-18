# 3 fibbonaci
n=int(input('enter number of terms: '))
n1=0
n2=1
count=0
if n<=1:
    print('enter valid terms')
elif n==1:
    print('fibbonaci series of 1 term is:',n1)
else:
    print('fibbonaci series are: ')
    while count< n:
        print(n1)
        n3=n1+n2
        n1=n2
        n2=n3
        count+=1