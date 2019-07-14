# --------------
import yaml

# Read the data of the format .yaml type
with open (path) as f:
        data = yaml.load(f)
f.close()

#print(data)
#print(data)

#print(team_1)
print("The Team 1 is" ,data['info']['teams'][0])
#print(team_2)
print("The Team 2 is" ,data['info']['teams'][1])
# Find data type of the file
print("The Type of data is",type(data))

# In which city, and at which venue the match was played and where was it played ?
print("The match was played in",data['info']['city'])

print('The Venue of the match was',data['info']['venue'])


# Which are all the teams that played in the tournament ? How many teams participated in total?
print("The match was between teams",data['info']['teams'][0],"and",data['info']['teams'][1])
# Which team won the toss and what was the decision of toss winner ?

# Find the first bowler and first batsman who played the first ball of the first inning

# How many deliveries were delivered in first inning ?

# How many deliveries were delivered in second inning ?

# Which team won and how ?



