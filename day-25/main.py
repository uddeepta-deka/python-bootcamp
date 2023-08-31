# with open("weather_data.csv", "r") as data_file:
#     data = data_file.readlines()
# print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
# print(temperatures)


import pandas

# data = pandas.read_csv("weather_data.csv")
# # print(data["temp"])
# data_dict = data.to_dict()
#
# # # average temperature
# # temperature_list = data["temp"].to_list()
# # average = sum(temperature_list)/len(temperature_list)
# # print(average)
# # print(data["temp"].max())
#
# # reading a row of data
# print(data[data.day == 'Monday'])
# print(data[data.temp == data.temp.max()].condition)

# create a dataframe from scratch
# data_dict = {
#     "students":["Aman", "Bunty", "Kashish"],
#     "scores":[80, 85, 95],
# }
#
# data = pandas.DataFrame(data_dict)
# print(data)

# read squirrel data
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_data = data["Primary Fur Color"].value_counts()
gray_squirrel_count = fur_data["Gray"]
red_squirrel_count = fur_data["Cinnamon"]
black_squirrel_count = fur_data["Black"]

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrel_count, red_squirrel_count, black_squirrel_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")


# print(squirrel_fur_data)
# data = pandas.DataFrame(squirrel_fur_data)
# data.to_csv("squirrel_count.csv")