# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv 

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     rows = list(data)
#     for row in rows[1:]:
#         temp = int(row[1])
#         temperatures.append(temp)

import pandas

# data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()
# #print(data_dict)
# temp_list = data["temp"].to_list()
# #print(temp_list)
# # avrg_temp = sum(temp_list) / len(temp_list)
# # print(avrg_temp)
# print(data["temp"].mean())
# print(data["temp"].max())
# print(data.condition)

# Get data in row 
# print(data[data.day == "Monday"])
# max_temp = data.temp.max()
# # print(data[data.temp == max_temp])

# monday = data[data.day == "Monday"]
# f_temp = monday.temp[0] * 1.8 + 32
# print(f_temp)

# create dataframe from scratch 

data_dict = {
    "students": ["Amy", "James", "Angela"], 
    "scroes": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")