import csv
import pandas

# with open("weather_data.csv", "r") as data:
#     content = csv.reader(data)
#     temperature = []
#     for item in content:
#         if item[1] != "temp":
#             temperature.append(int(item[1]))
#     print(temperature)

data = pandas.read_csv("weather_data.csv")
# print(data["temp"])

data_dic = data.to_dict()
print(data_dic)

temp_list = data["temp"].to_list()
avg_temp = sum(temp_list) / len(temp_list)
print(temp_list)
print(avg_temp)

mean = data["temp"].mean()
print(mean)

max = data["temp"].max()
print(max)

print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
m_temp = monday.temp
fahrenheit = (m_temp * 9 / 5) + 32
print(monday)
print(m_temp)
print(fahrenheit)

data_dict = {
    "students": ["Jack", "Jill", "Mark"],
    "scores": [99, 100, 98]
}

my_data = pandas.DataFrame(data_dict)
my_data.to_csv("my_data.csv")
print(my_data)