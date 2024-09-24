num = int(input("Please enter a number: "))
for i in range(1, num + 1):
    print(' ' * (num - i) + ' '.join(str(i) * i))

# In 1 line
# print('\n'.join(' ' * (num - i) + ' '.join(str(i) * i) for i in range(1, num + 1)))