
import json
import pandas as pd
import operator
import itertools

# Fantasy sheep - picks the most popular players

# Sum values at position
def sumpos(inp, pos):
    val = 0
    for entry in inp:
        element = entry[1][pos]
        val += element
    return val

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

data_dict = {}
names_dict = {}

for index,row in players_df.iterrows():
    popularity = float(row['selected_by_percent'])
    player_id = row['id']
    pos = row['element_type']
    name = row['second_name']
    price = row['now_cost']
    pp = popularity/price
    names_dict[player_id] = name
    data_dict[player_id] = [pos, popularity, price]
    #data_dict[player_id] = [pos, pp]
    
sorted_dict = sorted(data_dict.items(), key=operator.itemgetter(1), reverse=True)

gks = []
defs = []
mids = []
fwds = []
gk_limit = 5
def_limit = 10
mid_limit = 10
fwd_limit = 10

budget = 1000

# Get top players
for player in sorted_dict:
    # GK
    if player[1][0] == 1 and len(gks) < gk_limit:
        gks.append(player)
    # DEF
    if player[1][0] == 2 and len(defs) < def_limit:
        defs.append(player)
    # MID
    if player[1][0] == 3 and len(mids) < mid_limit:
        mids.append(player)
    # FWD
    if player[1][0] == 4 and len(fwds) < fwd_limit:
        fwds.append(player)
 
team_gks = [gks[0], gks[1]]
team_defs = [defs[0],defs[1],defs[2],defs[3],defs[4]]
team_mids = [mids[0],mids[1],mids[2],mids[3],mids[4]]
team_fwds = [fwds[0],fwds[1],fwds[2]]
val = 0
team_score = 0
team_val = 0

gk_combs = list(itertools.combinations(gks, 2))
def_combs = list(itertools.combinations(defs, 5))
mid_combs = list(itertools.combinations(mids, 5))
fwd_combs = list(itertools.combinations(fwds, 3))
# Try to find optimal team
for these_gks in gk_combs:
    print(team_val)
    gk_score = sumpos(these_gks, 1)
    gk_val = sumpos(these_gks, 2)
    for these_defs in def_combs:
        def_score = sumpos(these_defs, 1)
        def_val = sumpos(these_defs, 2)
        for these_mids in mid_combs:
            mid_score = sumpos(these_mids, 1)
            mid_val = sumpos(these_mids, 2)
            for these_fwds in fwd_combs:
                fwd_score = sumpos(these_fwds, 1)
                fwd_val = sumpos(these_fwds, 2)
                score = gk_score + def_score + mid_score + fwd_score
                val = gk_val + def_val + mid_val + fwd_val
                if score >= team_score and val <= 1000:
                    gks = these_gks
                    defs = these_defs
                    mids = these_mids
                    fwds = these_fwds
                    team_score = score
                    team_val = val
                



bench = []
starting_team = []

print('Value = {}'.format(team_val))
# Print team
print('Starting 11 : \n')
print(names_dict[gks[0][0]] + names_dict[gks[1][0]])
print(names_dict[defs[0][0]] + names_dict[defs[1][0]] + names_dict[defs[2][0]] + names_dict[defs[3][0]] + names_dict[defs[4][0]])
print(names_dict[mids[0][0]] + names_dict[mids[1][0]] + names_dict[mids[2][0]] + names_dict[mids[3][0]] + names_dict[mids[4][0]])
print(names_dict[fwds[0][0]] + names_dict[fwds[1][0]] + names_dict[fwds[2][0]])

print('Bench:')
print(bench)
    