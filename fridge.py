numbers = [str(x) for x in input()]
numbers.sort()

upper = 1000 * 9
lower = 1

for i in range(len(numbers)):
    



# smallest = 1
# while True:
#     smallest_str = list(str(smallest))
#     smallest_str.sort()
#     index = -1
#     for c in smallest_str:
#         try:
#             index = numbers.index(c, index + 1)
#         except ValueError:
#             index = -1
#             break
#     if index == -1:
#         break
#     else:
#         smallest += 1

print(smallest)