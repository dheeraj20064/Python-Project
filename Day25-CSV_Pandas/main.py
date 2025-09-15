# with open("weather_data.csv") as file:
#     data=file.readlines()
#     print(data)

# import csv
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1]!='temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

#import pandas
#data=pandas.read_csv("weather_data.csv")
#print(data["temp"])


# data_dict=data.to_dict()
# print(data_dict)
# temp_list=data["temp"].to_list()
# # avg=(sum(temp_list)/len(temp_list))
# # print(avg)
# print(data["temp"].mean())
# print(data["temp"].max())
# print(data.condition)
#print(data[data.day=="Monday"])

import pandas
data=pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250616.csv")
gray=(len(data[data["Primary Fur Color"]=="Gray"]))
black=(len(data[data["Primary Fur Color"]=="Black"]))
cinnamon=(len(data[data["Primary Fur Color"]=="Cinnamon"]))
new_data={
    "Fur colour":["gray","black","cinnamon"],
    "Count":[gray,black,cinnamon]
}
data_table=pandas.DataFrame(new_data)
data_table.to_csv("squirrel_count.csv")
