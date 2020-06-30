#Progam to find a solution for 8 Queens problem
import random
import sys

global n,maxFitness,pop_size

#Function to generate initial population
def populate():
  pop_list=[]
  n=8
  maxFitness = (n*(n-1))/2 
  pop_size= 100
  for i in range(pop_size):
    population = random.sample(range(0,n), n)
    pop_list.append(population)
  # print(pop_list)
  return pop_list

#Function to select randomly from population
def rand_select(pop_list):
  selected_element = random.choice(pop_list)
  fitscore = calc_fitness(selected_element)
  return(selected_element,fitscore)

#Function to reproduce two randomly selected chromosomes
def reproduce(x,y):
  n = len(x)
  c = random.randint(0, n - 1)
  child= x[0:c] + y[c:n]
  # print(child)
  return child

#Function to mutate a child
def mutate(child):  
  n = len(child)
  c = random.randint(0, n - 1)
  m = random.randint(1, n-1)
  child[c] = m
  mutated_child= child
  return mutated_child
  # print('mutated-',child)

#Function to calculate Fitness
def calc_fitness(chrome):
  horizontal_collisions = sum([chrome.count(queen)-1 for queen in chrome])/2
  # print(chrome,[chrome.count(queen)-1 for queen in chrome],horizontal_collisions)
  diagonal_collisions = 0

  n = len(chrome)
  left_diagonal = [0] * 2*n
  right_diagonal = [0] * 2*n
  for i in range(n):
      left_diagonal[i + chrome[i] - 1] += 1
      right_diagonal[len(chrome) - i + chrome[i] - 2] += 1
  diagonal_collisions = 0
  for i in range(2*n-1):
      counter = 0
      if left_diagonal[i] > 1:
          counter += left_diagonal[i]-1
      if right_diagonal[i] > 1:
          counter += right_diagonal[i]-1
      diagonal_collisions += counter / (n-abs(i-n+1))
  fit= maxFitness - (horizontal_collisions + diagonal_collisions)
  return(fit)

#Genetic Algorithm function
def genetic_queen(pop_list):
  new_population = []

  for i in range(0,pop_size):
    x,fitx = rand_select(pop_list)
    y,fity = rand_select(pop_list)

    child = reproduce(x,y) #Reproduction is done here
    mutated_child = mutate(child) #Mutation is done here
    new_population.append(mutated_child)
    mut_fitness = calc_fitness(mutated_child)
    if  mut_fitness == maxFitness: 
      # print(mutated_child,mut_fitness,maxFitness)
      nofitfound= False
      break
    else:
      nofitfound = True
    
  return(new_population,nofitfound)

#Main Function
if __name__ == "__main__":
  pop_list=populate()
  nofitfound =  False
  new_population,nofitfound=genetic_queen(pop_list)
  # print(nofitfound)
  while nofitfound == True:
    new_population,nofitfound=genetic_queen(pop_list)
  for chrom in new_population:
    fit=calc_fitness(chrom)
    if fit==maxFitness:
      print('Selected Chromosome-',chrom,'\nFitness-',fit)
      break
