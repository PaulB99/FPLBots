import json
import pandas as pd
import operator
import itertools
import random
import csv

# Fantasy pigeon - just choose a random team, then make random transfers

# Load in data
with open('../data/players_data.json') as json_file:
    players = json.load(json_file)

with open('../data/teams_data.json') as json_file:
    teams = json.load(json_file)
    
with open('../data/events_data.json') as json_file:
    events = json.load(json_file)
    
with open('../data/my_team.json') as json_file:
    my_team = json.load(json_file)

# Create pandas dataframes
players_df = pd.DataFrame(players)
teams_df = pd.DataFrame(teams)  
events_df = pd.DataFrame(events)

# CONTROL PANEL
new = False
gw = 1

gks = []
max_gks = 2
defs = []
max_defs = 5
mids = []
max_mids = 5
fwds = []
max_fwds = 3

if new:
    players = []
    for index,row in players_df.iterrows():
        name = row['second_name'] + ' ' + str(row['team'])
        pos = row['element_type']
        players.append([name,pos])
        
    done = False
    while not done:
        player = random.choice(players)
        if player[1] == 1 and len(gks) < max_gks:
            gks.append(player[0])
        elif player[1] == 2 and len(defs) < max_defs:
            defs.append(player[0])
        elif player[1] == 3 and len(mids) < max_mids:
            mids.append(player[0])
        elif player[1] == 4 and len(fwds) < max_fwds:
            fwds.append(player[0])
        elif len(gks) == max_gks and len(defs) == max_defs and len(mids) == max_mids and len(fwds) == max_fwds:
            done = True
            
    #Save team to file  
    with open('teams/team' + str(gw) + '.csv', mode='w') as team_file:
        writer = csv.writer(team_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for x in gks:
            newtuple = (x, 1)
            writer.writerow(newtuple)
        for x in defs:
            newtuple = (x, 2)
            writer.writerow(newtuple)
        for x in mids:
            newtuple = (x, 3)
            writer.writerow(newtuple)
        for x in fwds:
            newtuple = (x, 4)
            writer.writerow(newtuple)
    print('Team: ')
    for x in gks:
        print(x)
    for x in defs:
        print(x)
    for x in mids:
        print(x)
    for x in fwds:
        print(x)
    print('Bench the following: ')
    print(random.choice(gks))
    counter = 0
    while counter<3:
        p = random.randint(2, 4)
        if p == 2:
            print(random.choice(defs))
        elif p == 3:
            print(random.choice(mids))
        elif p == 4:
            print(random.choice(fwds))
        counter+=1
    
        