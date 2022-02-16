import random
from creature import Creature
from genome import Genome
# Code written Terminologies
# CamalCase used for Functions/Methods
# Snake Case used for variables

# parameters
population_size=100
genome_size=4
world_size=128 # Square World
step_per_gen=300 # Age
mutation=0.0 # range 0.0-1.0

# initializing creatures
location_array=[]
population_array=[]

# all possible locations
for x in range(world_size):
    for y in range(world_size):
        location_array.append((x,y))
# print(location_array)

for i in range(population_size):
    loc=location_array.pop(random.randint(0,world_size*world_size-1))
    population_array.append(Creature(Genome(size=genome_size),loc))

for creaturetime in range(step_per_gen):
    for creature in population_array:
        creature.grow()# to iteratrate once
# after this loop creature have finished there first lifecycle
# here i have to store the data from genertion 1
