avg = 9 * 365 / 12
salary = int(input("How much is your monthly income?\n"))
t = {}
bills = {}
while True:
    print("Enter your expensis per months\n"
          "[A] Bills\n"
          "[B] Food\n"
          "[C] Rent\n"
          "[D] Others\n"
          "[X] Exit\n")
    op = input()
    if op == "a".lower():
        p_amount = int(input("Enter the amount"))
        p_amount = t.add(p_amount)
    print(t)


#print(bills)
# print(f"You should be able to put on the side {int(salary) - avg}£ per months")