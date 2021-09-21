# Easy Approach 

s1=input()
s2=input()
s1=set(s1)
s2=set(s2)
s=s1&s2
print(len(s))


# Normal approach

# s1=input()
# s2=input()
# s=[]
# count=0
# for i in s1 :
#     for j in s2 :
#         if i==j and (i not in s):
#             count+=1
#             s.append(i)
#             break
# print(count)
