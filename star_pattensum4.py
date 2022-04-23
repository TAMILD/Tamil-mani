# star patten 1:
n=int(input("Enter the velue:"))
for i in range(1,n+1,1):
    st='*'*i
    print(st)
for i in range(n-1,0,-1):
    st1='*'*i
    print(st1)    
# star patten 2:    
n=int(input("Enter the velue:"))
for i in range(1,n+1,1):
    st='*'*i
    st=st.rjust(n)
    print(st)
for i in range(n-1,0,-1):
    st1=('*'*i)
    st1=st1.rjust(n)
    #st1=st1.replace(' ',"-")
    print(st1)    
    