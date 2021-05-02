"""Import Libraries and Frameworks"""

# import random
# import operator
import matplotlib.pyplot
from agentframework import Agent
import time
import csv

"""Initial Setup and Parameters"""

start = time.time() # start time counter

rowlist = [] # this creates an empty row list
environment=[] # this creates an empty environment list
num_of_agents = 100 # this limits the number of agents
num_of_iterations = 10
neighbourhood = 20
agents = [] # this creates an empty agents list

"""Environment CSV"""

f = open('in.txt', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader:
    rowlist = []
    environment.append(rowlist)
    for value in row:
        rowlist.append(value) # fill the environment list
        
f.close()

"""Verify that Environment has Imported Correctly"""

matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()

"""Distance Between Agents"""

def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) +
            ((agents_row_a.y - agents_row_b.y)**2))**0.5

"""Make the Agents"""

for i in range(num_of_agents): # this fills the list of agents
    agents.append(Agent(environment, agents, 2, 3))

"""Call and Loop Through the Agents"""

for j in range (num_of_iterations):
    for i in range (num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood) 
        
"""Generate Scatter Graph of Agents"""

matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()

                
"""Verify that agentframework imported correctly"""

a = Agent(environment, agents, 2, 3)
print(a.y, a.x) # show original agents
a.move() # move the agents
print(a.y, a.x) # show moved agents

"""Output to .CSV"""

f2 = open('output.csv','w',newline='')
writer = csv.writer(f2, delimiter = ' ')

for row in environment:
    writer.writerow(row)
f2.close()


"""Check Timing"""

end = time.time() # end time counter
print(end - start) # processing time in seconds