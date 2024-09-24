num = int(input("Enter a number: "))

# # Negative numbers, 0 and 1 are not primes
# if num <=1:
#     print(num, "is not a prime number")
#     exit()

# i = 2
# while i <= int(num**0.5):
#     if num % i == 0:
#         print(num, "is not a prime number")
#         exit()
#     i+=1

# print(num, "is prime number")

# In one line
print(num, "is prime number") if num > 1 and all(num % i != 0 for i in range(2, int(num**0.5)+1)) else print(num, "is not a prime number")