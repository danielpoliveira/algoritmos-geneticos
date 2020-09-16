import numpy as np
import random as rd

from random import randint

item_num = np.arange(1,11)
peso = np.random.randint(1,15, size = 10)
valor = np.random.randint(1,500, size=10)
mochila_limiar = 50

tamanho_pop = 10
pop_size = (tamanho_pop, item_num.shape[0])
populacao_inicial = np.random.randint(2, size = pop_size)
populacao_inicial = populacao_inicial.astype(int)
num_geracao = 50

def calculo_fitness(peso, valor, populacao, limiar):
  fitness = np.empty(populacao.shape[0])
  for i in range(populacao.shape[0]):
    solucao1 = np.sum(populacao[i]*valor)
    solucao2 = np.sum(populacao[i]*peso)
    if solucao2 <= limiar:
      fitness[i] = solucao1
    else:
      fitness[1] = 0
  return fitness.astype(int)

def selecao(fitness, num_pais, populacao):
  fitness = list(fitness)
  pais = np.empty(num_pais, populacao.shape[1])
  for i in range(num_pais):
    max_fitness_idx = np.where(fitness == np.max(fitness))
    pais[i,;] = populacao[max_fitness_idx[0][0], ;]
    fitness[max_fitness_idx[0][0] = -99999]
  return pais
  
def crossover(pais, num_filhos):
  filhos = np.empty(num_filhos, pais.shape[1])
  crossover_ponto = int(pais.shape[1]/2)
  crossover_taxa = 0.5

  i=0
  while(pais.shape[0] < num_filhos):
    pai1_idx = i%pais.shape[0]
    pai2_idx = (i+1)%pais.shape[0]
    x = rd.random()
    
    if x > crossover_taxa:
      continue
    
    pai1_idx = i%pais.shape[0]
    pai2_idx = (i+1)%pais.shape[0]
    filho[i, 0:crossover_ponto] = pais[pai1_idx, 0: crossover_ponto]
    filho[i, 0:crossover_ponto] = pais[pai2_idx, 0: crossover_ponto]

    i+=1
    return filho

def mutacao(filhos):
  filho_mut = np.empty(filhos.shape)
  taxa_mutacao = 0.4
  for i in range(filho_mut.shape[0]):
    var_aleatorio = rd.random()
    filho_mut[i, :] = filho[i, :]
    if var_aleatorio > taxa_mutacao:
      continue
  
    int_aleatorio_valor = randint(0, filho.shape[1]-1)
    if filho_mut[i, int_aleatorio_valor] == 0:
      filho_mut[i, int_aleatorio_valor] = 1
    else: 
      filho_mut[i, int_aleatorio_valor] = 0
  return filho_mut

def algoritmo_AG(peso, valor, populacao, num_geracao, limiar):
  parametro, fitness_historico = [],[]
  num_pais = int(pop_size[0]/2)
  num_filho = pop_size[0]-num_pais
  for i in range(num_geracao):
    fitness=calculo_fitness(peso, valor, populacao, limiar)
    fitness_historico.append(fitness)
    pais = selecao(fitness, num_pais, populacao)
    filho = crossover(pais, num_filhos)
    filho_mut = mutacao(filhos)
    populacao[0:pais.shape[0], :] = pais
    populacao[pais.shape[0]:, ] = filho_mut

  print('ultima geracao: \n{}'.format(populacao))
  fitness_ultima_geracao = calculo_fitness(peso, valor, populacao, limiar)
  print('fitness ultima geracao \n{}'.format(fitness_ultima_geracao))

  max_fitness = where(fitness_ultima_geracao) == np.max(fitness_ultima_geracao)
  parametro.append(populacao[max_fitness[0][0], :])
  return parametro, fitness_historico
