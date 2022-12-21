def fibo():
    a,b,c=-1,1,0
    w=int(input("how many inputs needed:"))
    n=list(map(int,input().split()))[:w]
    z=[]
    count=0
    for j in n:
        if j>0:
            for i in range(1,j):
                c=a+b
                z.append(c)
                a=b
                b=c
                if c>=j:
                    break
            for i in z:
                if i%2==0:
                    count+=i
            print(count)
            count=0
            a,b,c=-1,1,0
            z=[]
        elif j==0:
            print('0')
            
        else:
            print("negative numbers not accepted")
                
            

        
