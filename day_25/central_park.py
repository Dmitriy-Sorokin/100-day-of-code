import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

all_color = data["Primary Fur Color"].to_list()

color_g = []
color_c = []
color_b = []

for color in all_color:
    if color == "Gray":
        color_g.append(color)
    elif color == "Black":
        color_b.append(color)
    elif color == "Cinnamon":
        color_c.append(color)

dict_color = {
    "Ful Color": [],
    "Count": []
}
dict_color["Ful Color"].append(color_g[0])
dict_color["Ful Color"].append(color_c[0])
dict_color["Ful Color"].append(color_b[0])

dict_color["Count"].append(len(color_g))
dict_color["Count"].append(len(color_c))
dict_color["Count"].append(len(color_b))

print(dict_color)

new_data_d = pandas.DataFrame(dict_color)
new_data_d.to_csv("squirrel_count.csv")
