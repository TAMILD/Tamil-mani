n=int(input("Enter the velue:"))
for i in range(1,n+1,1):
    st='*'*i
    st1=st.ljust(n)
    st2=st.rjust(n)
    st=st1+st2[1::]
    st=st.replace(' ',"-")
    print(st)
n=int(input("Enter the velue:"))
for i in range(n,0,-1):
    st='*'*i
    st1=st.ljust(n)
    st2=st.rjust(n)
    st=st1+st2[1::]
    #st=st.replace(' ',"_")
    print(st)