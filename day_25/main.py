# with open("weather_data.csv") as weather_data:
#     list_weather_data = weather_data.readlines()
#     print(list_weather_data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         # if row[1] != "temp":
#             temp_int = row[1]
#             int_data = int(temp_int)
#             temperatures.append(int_data)
#             print(row)
#
# print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
#
# sum_list = sum(temp_list) / len(temp_list)
#
# print(sum_list)
# # Get data columns
# print(data["temp"].max())
# print(data.temp)
# # Get data row

monday = data[data.day == "Monday"]
t_m = monday.temp
far = 9/5 * t_m + 32
print(far)
print(t_m)
max_day = data["temp"].max()
print(data[data.temp == max_day])

# Crate a dadaframe from scratch

data_dict = {
    "student": ["Ann", "Ben"],
    "score": [50, 20]
}

data_d = pandas.DataFrame(data_dict)
print(data_d)
data_d.to_csv("new_data.csv")
