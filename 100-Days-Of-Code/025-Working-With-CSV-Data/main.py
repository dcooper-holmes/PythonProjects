
# Below is a comparison of using Pandas vs not using Pandas

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# import pandas

# data = pandas.read_csv("weather_data.csv")
# temp_list = data["temp"].to_list()
# #print(temp_list)
#
# # Pandas has a lot of useful functions. We can get things such as the average and the highest from the Data Frame.
# #print(data["temp"].mean())
# #(data["temp"].max())
#
# # You can also target specific data by using the .'column header/title': data.day
# #print(data.day)
#
# # You can also get specific data for specific row:
# #print(data[data.day == "Monday"])
# #print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# monday_temp_c = monday.temp
# monday_temp_f = monday.temp * 9/5 + 32
# print(monday_temp_c)
# print(monday_temp_f)

#--Squirrel Fur Colour CSV Challenge--

import pandas

data = pandas.read_csv("squirrel_data.csv")

num_grey_squirrel = len(data[data["Primary Fur Color"] == "Gray"])
num_cinnamon_squirrel = len(data[data["Primary Fur Color"] == "Cinnamon"])
num_black_squirrel = len(data[data["Primary Fur Color"] == "Black"])

squirrel_dict = {
    "Fur Color": ["Grey", "Cinnamon", "Black"],
    "Count": [num_grey_squirrel, num_cinnamon_squirrel, num_black_squirrel]
}

df = pandas.DataFrame(squirrel_dict)
df.to_csv('./New_Squirrel_Fur_Data.csv')