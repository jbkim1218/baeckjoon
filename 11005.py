n,b = map(int,input().split())
ans = ""
while n!=0:
    a = n % b
    if a >= 10:
        ans += chr(a+55)
    else:
        ans += str(a)
    n //= b
print(ans[::-1])