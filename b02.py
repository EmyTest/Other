from __future__ import print_function
# for i in range(1,5):
#     for j in range(1,6):
#         if i==1 or i==4 or j==1 or j==5:
#             print('*',end =" ")
#         else:
#             print(' ',end=" ")
#     print()

for i in range(1,6):
    for j in range(1,7-i):
        if i==1 or i==5 or j==1 or j==7-i-1:
            print('*',end =" ")
        else:
            print(' ',end=" ")
    print()