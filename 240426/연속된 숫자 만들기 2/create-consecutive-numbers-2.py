a,b,c = map(int,input().split())

# cnt = 0
# while b-a>1 or c-b>1:
#     if b-a!=1 and b-a<=c-b or c-b==1 :
#         c = a+(b-a)//2
#         b,c = c,b
#         cnt+=1
#     else:
#         a = b+(c-b)//2
#         a,b = b,a
#         cnt+=1
#         print(a,b,c)


# print(cnt)


if a+1 == b and a+2==c:
    print(0)
elif a+2 == b or b+2==c:
    print(1)
else:
    print(2)