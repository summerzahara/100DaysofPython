import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_color = data["Primary Fur Color"]
fur_color_list = fur_color.to_list()

fur_color_types = list(set(fur_color_list))
fur_color_count = []

for item in fur_color_types:
    count = fur_color_list.count(item)
    fur_color_count.append(count)

squirrel_dict = {
    "Fur Color": fur_color_types,
    "Count": fur_color_count
}

squirrel_count = pandas.DataFrame(squirrel_dict)
squirrel_count.to_csv("squirrel_count.csv")

print(fur_color_list)
print(fur_color_types)
print(fur_color_count)
print(squirrel_dict)

