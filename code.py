# --------------
import numpy as np
import pandas as pd
import csv

# Not every data format will be in csv there are other file formats also.
 # This exercise will help you deal with other file formats and how to read it.
with open(path, newline='') as csvfile:
    data = np.array(list(csv.reader(csvfile)))

# Number of unique matches 
 # How many matches were held in total we need to know so that we can analyze further statistics keeping that in mind. 

match_code = np.unique(data[1:,0]).shape[0]
print(f'The unique number of matches played in IPL are {match_code}')

# Number of unique teams
 # this exercise deals with you getting to know that which are all those six teams that played in the tournament.

team1 = data[1:,3:4] 
team2 = data[1:,4:5] 
teams = np.unique(np.core.defchararray.add(team1, team2)).shape[0] 
print(f'Total number of match held in IPL were {teams}') 

# Sum of all extras
 # An exercise to make you familiar with indexing and slicing up within data.

extras = np.sum(list(map(float, data[1:,17:18])), 0) 
print(f'Total number of extras in all deliveries of IPL is {int(extras)}')   

# Delivery number when a given player got out
 # Get the array of all delivery numbers when a given player got out. Also mention the wicket type.
df = pd.read_csv(path)

delivery_out = df[df['wicket_kind'].notnull()]['delivery'].values
wicket_type = df[df['wicket_kind'].notnull()]['wicket_kind'].values
print(f'The delivery numbers when a player got out are {delivery_out} and the wicket type for those players are {wicket_type}')

# Number of times Mumbai Indians won the toss
 # This exercise will help you get the statistics on one particular team

MI_toss_win_count = df[df['toss_winner'] == 'Mumbai Indians']['match_code'].values
print('Number of times Mumbai Indians won the toss is {}'.format(np.unique(MI_toss_win_count).shape[0])) 

# Filter record where batsman scored six and player with most number of sixex
 # An exercise to know who is the most aggresive player or maybe the scoring player 

batsman_scored_six = df[df['runs'] == 6]['batsman'].values
print(f'Number of sixes scored by batsman is {batsman_scored_six.shape[0]}')

unique, counts = np.unique(batsman_scored_six, return_counts = True)
batsman_scored_max_six = unique[np.argsort(counts)][28:] 
 
print(f'The batsman who scores maximum number of sixes are {list(batsman_scored_max_six)}')
 
