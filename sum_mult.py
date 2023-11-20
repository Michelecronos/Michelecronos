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

print("Printing current and previous number and their sum in a range(10)")
num1 = 0
num2 = 0
for num1 in range(0, 10):
    sum_numb = num1 + num2
    print(f"Current number {num1} Previous number {num2} Sum: {sum_numb}")
    num1 += 1
    num2 = num1 - 1


str_word = input("Enter word: ")
print("Original String is ", str_word)
size = len(str_word)
print("Printing only even index chars")
for i in range(0, size-1, 2):
    print("index[", i, "]", str_word[i])


def remove_chars(word, n):
    print('Original string:', word)
    x = word[n:]
    return x


print("Removing characters from a string")
print(remove_chars("pynative", 4))
print(remove_chars("pynative", 2))


def first_last_same(numberList):
    print("Given list:", numberList)

    first_num = numberList[0]
    last_num = numberList[-1]

    if first_num == last_num:
        return True
    else:
        return False


numbers_x = [10, 20, 30, 40, 10]
print("result is", first_last_same(numbers_x))

numbers_y = [75, 65, 35, 75, 30]
print("result is", first_last_same(numbers_y))


