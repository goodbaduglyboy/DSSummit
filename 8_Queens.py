#Progam to find a solution for 8 Queens problem
import random
import sys
import numpy as np

#Function to generate initial population
def populate():
  global n,maxFitness,pop_size
  pop_list=[]
  n=8
  maxFitness = (n*(n-1))/2 
  pop_size= 100
  for i in range(pop_size):
    population = random.sample(range(0,n), n)
    pop_list.append(population)
  
  return pop_list

#Function to select randomly from population
def rand_select(pop_list):
  selected_element = random.choice(pop_list)
  fitscore = calc_fitness(selected_element)
  return(selected_element,fitscore)

#Function to reproduce two chromosomes
def reproduce(x,y):
  n = len(x)
  c = random.randint(0, n - 1)
  child= x[0:c] + y[c:n]
  
  return child

#Function to mutate a child
def mutate(child):  
  n = len(child)
  c = random.randint(0, n - 1)
  m = random.randint(1, n-1)
  child[c] = m
  mutated_child= child
  return mutated_child
  

#Function to calculate Fitness
def calc_fitness(chrome):
  l = chrome
  clashes = 0
  row_clashes = abs(len(l)-len(np.unique(l)))
  

  for i in range(len(l)):
    for j in range(len(l)):
      if(i!=j):
        dx = abs(i-j)
        dy = abs(l[i]-l[j])
        if(dx==dy):
          clashes=clashes+1

  clashes= clashes+row_clashes
  fit= maxFitness - clashes
  return fit
  

#Genetic Algorithm function
def genetic_queen(pop_list):
  new_population = []

  for i in range(0,pop_size):
    x,fitx = rand_select(pop_list) #Selection at work
    y,fity = rand_select(pop_list)

    child = reproduce(x,y) #Reproduction is done here
    child = mutate(child) #Mutation is done here
    new_population.append(child)
    mut_fitness = calc_fitness(child)
    if  mut_fitness == maxFitness: 
  
      nofitfound= False
      break
    else:
      nofitfound = True
    
  return(new_population,nofitfound)

# Main Function
if __name__ == "__main__":
  
  pop_list=populate()
  nofitfound =  False
  new_population,nofitfound=genetic_queen(pop_list)
  
  while nofitfound == True:
    new_population,nofitfound=genetic_queen(pop_list)
  for chrom in new_population:
    fit=calc_fitness(chrom)
    if fit==maxFitness:
      print('Selected Chromosome-',chrom,'\nFitness-',fit)
      break
