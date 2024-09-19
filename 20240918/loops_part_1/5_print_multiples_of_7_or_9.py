    # for i in range(1, 101):
#     if i % 7 == 0 or i % 9 == 0:
#         print(i)
      
i = 1 
while i < 101:
    if i % 7 == 0 or i % 9 == 0:
        print(i)
        i += 1

# In 1 line
# [print(i) for i in range(1, 101) if i % 7 == 0 or i % 9 == 0]