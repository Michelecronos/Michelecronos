def multiplican_and_sum(num1, num2):
    product = num1 * num2
    if product <= 1000:
        return product
    else:
        return num1 + num2

result = multiplican_and_sum(20, 30)
print("The result is", result)

result = multiplican_and_sum(40, 30)
print("The result is", result)