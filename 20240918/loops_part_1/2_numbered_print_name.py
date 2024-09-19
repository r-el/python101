name = input("What is your name? ")

i = 1
while i<=100:
    print(f"{i}. {name}")
    i += 1
    
# In 1 line
# [print(f"{i}. {name}") for i in range(1, 101)]
