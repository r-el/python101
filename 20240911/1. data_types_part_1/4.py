# a. 0
# b. 1
# c. -1
# d. ‘False’
# e. False

values = [0, 1, -1, 'False', False]

for value in values:
    boolean_value = bool(value)
    print(f"{value} is {boolean_value}")

if bool(0) == False:
    print("We were right about 0")
else:
    print("We were wrong about 0")

if bool(1) == True:
    print("We were right about 1")
else:
    print("We were wrong about 1")

if bool(-1) == True:
    print("We were right about -1")
else:
    print("We were wrong about -1")

if bool('False') == True:
    print("We were right about 'False'")
else:
    print("We were wrong about 'False'")

if bool(False) == False:
    print("We were right about False")
else:
    print("We were wrong about False")