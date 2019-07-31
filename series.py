a='111213311'
a_list=list(a)
#print(a_list)
b='3112112321'
items=[]
test={}
for i in range(len(a_list)-1):

    if(a[i]!=a[i+1]):
        test[a[i+1]] = 1

    else:
        test[a[i]] += 1

print(type(test[a[0]]))

# last=''
# results=[]
# word=a
# for letter in word:
#     if (letter==last):
#         results[-1]=(letter,results[-1][1]+1)
#     else:
#         results.append((letter,1))
#         last=letter
# print(results,len(results))
# final=[]
# for i in range(len(results)):
#     final.append(results[i][1])
#     final.append(results[i][0])
# final=list(map(str,final))
# print(''.join(final))
