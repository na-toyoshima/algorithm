number = int(input("input:"))

result = ''

while number > 0:
    result = str(number % 2) + result
    number //= 2

print(result)

