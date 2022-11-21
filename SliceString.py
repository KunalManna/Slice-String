#input-1>  Today
#Output->  doTday

#input-1>  nice
#Output->  ince



def SliceString(s):
    n=len(s)
    if n%2!=0:
        a=s[n//2::-1]
        b=s[n//2::]
        c=a+b
        return c
    else:
        x=s[n//2-1::-1]
        y=s[n//2::]
        z=x+y
        return z

s=input("Enter the string:\n")
ans=SliceString(s)
print(ans)