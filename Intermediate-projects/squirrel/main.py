import pandas
data = pandas.read_csv("2018_Squirrel_Data.csv")
data.dropna()

colors = set(list(data["Primary Fur Color"].dropna()))

data_dict = {}

for color in colors:
    rows = data[data["Primary Fur Color"] == color]
    data_dict[color] = len(rows)

print(data_dict)

new_data = pandas.DataFrame(list(data_dict.items()), columns=['Fur Color', 'Count'])

new_data.to_csv("sanitize.csv")




