# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#         print(row)
#
# print(temperatures)

import pandas

# data = pandas.read_csv('weather_data.csv')
# print(data)
#
# temp_list = data['temp'].tolist()
# print(f"Average", sum(temp_list) / float(len(temp_list)))
#
# print(data['temp'].mean())
# print(data['temp'].max())
#
# # Get Data in row
# print(data[data.day == "Monday"])
#
# monday = data[data.day == "Monday"]
# print(monday)

# Fur Color, Count
data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
gray_squirrel = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrel = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", 'Black'],
    "Count": [gray_squirrel, cinnamon_squirrel, black_squirrel]

}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")

print(data_dict)
