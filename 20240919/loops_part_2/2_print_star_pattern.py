num = int(input("Please enter a number: "))

for i in range(1, num+1):
    print("* "*i)

# it works for the other way around as well
for i in range(num-1,0,-1):
    print("* "*i)

# In 1 line (Using modulus for the 2 loops)
# num  = int(input("Please enter a number: "))
# [print("* "*i) for i in range(1, num+1)] + [print("* "*i) for i in range(num-1,0,-1)]
