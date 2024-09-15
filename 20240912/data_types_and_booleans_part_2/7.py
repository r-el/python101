# a)
is_true = False
is_false = True
result_a = is_false and (is_true or not is_false) and not (is_false and is_true)
print("a) Result:", result_a)

# b)
age = 25
has_license = True
has_experience = False
is_eligible = False
result_b = age >= 18 and (has_license or has_experience) and not is_eligible
print("b) Result:", result_b)

# c)
pi = 3.14159
count = 10
max_count = 15
is_greater_than_pi = pi > 3.0
is_in_range = count >= 0 and count <= max_count
result_c = is_greater_than_pi or (is_in_range and not (count < max_count))
print("c) Result:", result_c)

# d)
grade = "B"
Score = 90
score = 80
is_passing = grade == 'A' or (grade == 'B' and score >= 70)
is_excellent = grade == 'A' and score >= 90
result_d = is_passing and not is_excellent
print("d) Result:", result_d)

# e)
a = 5
b = 3
c = 2
condition1 = a > b
condition2 = c != 0
result_e = (condition1 or condition2) and (a % c == 0)
print("e) Result:", result_e)