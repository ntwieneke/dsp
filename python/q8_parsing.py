#The football.csv file contains the results from the English Premier League. 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 

# The below skeleton is optional.  You can use it or you can write the script with an approach of your choice.


# import csv

import pandas as pd

df = pd.read_csv('python/football.csv')
df.head()

df['Goal_Spread'] = (df['Goals'].sub(df['Goals Allowed'])).abs()
df['Goal_Spread']

lowest_spread = df['Goal_Spread'].argmin()
print lowest_spread

print df.loc[7]['Team'] 
print df.loc[7]['Goal_Spread']


# def read_data(data):
#   	with open(data, 'r') as data_open:
# 		parsed_data = [row for row in csv.reader(data_open.read().splitlines())]
# 	return parsed_data	
#    # COMPLETE THIS FUNCTION

# def get_min_score_difference(self, parsed_data):

#     # COMPLETE THIS FUNCTION

# # def get_team(self, index_value, parsed_data):
# #     # COMPLETE THIS FUNCTION

# print read_data("football.csv")