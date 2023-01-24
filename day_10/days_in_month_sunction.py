def is_leap(inp_year):
    if inp_year % 4 == 0:
        if inp_year % 100 == 0:
            if inp_year % 400 == 0:
                leap_year = True
            else:
                leap_year = False
        else:
            leap_year = True
    else:
        leap_year = False
    return leap_year


def days_in_month(inp_year, inp_month):
    # If it is a leap year, change 1 object in the list to 29
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap = is_leap(inp_year)
    if leap:
        month_days[1] = 29
        int_mount = int(inp_month)
        return month_days[int_mount - 1]
    else:
        int_mount = int(inp_month)
        return month_days[int_mount - 1]


# 🚨 Do NOT change any of the code below
year = 2024  # int(input("Enter a year: "))
month = 2  # int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
