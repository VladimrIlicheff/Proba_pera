# print("x y z w") 
# for x in range(2):
#   for y in range(2):
#    for z in range(2):
#     for w in range(2):
#       if not ((w and z) or not y or (not x == (not w))):
#         print(x, y, z, w)
n = int(input())
m = int(input())

if n == m ** 2 or m == n ** 2:
 print("Yes")
else:
 print("No")