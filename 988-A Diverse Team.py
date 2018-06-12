
'''


Hagar Osama : 12 / 6 / 2018

'''

#take n: no of students , k: size of team
from typing import List

n, k = input().split()


n = int(n)
k = int(k)
o = k


#take inputs from User:
students = [int(x) for x in input().split()]
index: List[int] = []


s = []
for i in students:
       if k == 0:
           break

       if i not in s:
         s.append(i)
         k = k-1
         index.append(students.index(i)+1)


if index.__len__() == o:
    print("YES")

    print(' '.join(map(str, index)))
else :
    print("NO")


