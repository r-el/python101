# shgiaa: NameError: name 'value' is not defined
# tikun: להדפיס את הערך שנמצא במשתנה result ולא במשתנה value
def multiply_by_two(value):
    value = value * 2
    return value

result = multiply_by_two(10)
print(value)