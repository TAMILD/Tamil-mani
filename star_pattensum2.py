#model star pattensum 1:
a=int(input("Enter the number:"))
for i in range(a,0,-1):
    st='*'*i
    st=st.rjust(a)
    print(st)
#model star patten sum 2:
a=int(input("Enter the number:"))
for i in range(a,0,-1):
    st='*'*i
    st=st.ljust(a)
    print(st)