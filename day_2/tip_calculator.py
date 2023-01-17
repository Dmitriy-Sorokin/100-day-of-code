bill = float(input("Welcome to the tip calculator!\nWhat was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
split_people = int(input("How many people to split the bill? "))
bill_with_proc = tip / 100 * bill + bill
total_bill = bill_with_proc / split_people

final_amount = "{0:.2f}".format(total_bill)
print(f"Счёт поделенный на всех состовляет {final_amount}!!!")
