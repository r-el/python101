# for i in range(1, 1001):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FuzzBuzz")
#     elif i % 3 == 0:
#         print("Fuzz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)

# In one line
# [print("FuzzBuzz") if i % 3 == 0 and i % 5 == 0 else print("Fuzz") if i % 3 == 0 else print("Buzz") if i % 5 == 0 else print(i) for i in range(1, 1001)]