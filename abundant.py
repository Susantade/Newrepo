#abundant number between a given range
class abundant:
    def abun(self,x,y):
        self.x=x
        self.y=y
        for j in range(x,y+1):
            s=0
            for i in range(1,j):
                if j%i==0:
                    s+=i
            if s>j:print(j,end=' ')
a=int(input('Enter the first number:'))
b=int(input('Enter the last number:'))
if a<=0 or b<=0:
    print('Please,enter valid range')
else:
    print('The abundant numbers between',a,'and',b,'are:')
    obj=abundant()
    obj.abun(a,b)
    
