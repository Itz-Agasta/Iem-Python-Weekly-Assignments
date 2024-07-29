#q1

n = input("enter a no. :")
n=list(n)
temp=n[-3]
n[-3]=n[-1]
n[-1]=temp
n=''.join(n)
print(n)



#q2

n = input("Enter a number:")
d=n[-2]
d=int(d)*2
n=list(n)
n[-2]=d
s=''
for i in n:
    s=s+str(i)

print(s)



#q3

n = input("Enter a number:")
s=''
for i in n:
    if i=='.':
        s=s+i+'1'
    else:
        s=s+i

print(s)


#q4

n = input("Enter a number:")
s=''
for i in n:
    if i=='.':
        s=s+'1'+i
    else:
        s=s+i

print(s)



#q5

s = input("Enter a number:")
c=0
for i in s[:-1]:
    if i == '.':
        print(s[c+1])
    c+=1

