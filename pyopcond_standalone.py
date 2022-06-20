import numpy as np
import math

# + ========================================= +

# Variable Interval Scheduling Generator
# Utilizes the Hoffman-Fleshler Constant Probability Distribution
    # Based on Hantula (1991) and Fleshler et Hoffman (1962)
# Program Parameters
    # N = Amount of terms
    # m = mean
    # n = the nth term of progression
def var_int(N, mean):
    var_int.new_array = []
    var_int.progression = list(range(1, N, 1))
    var_int.progression.append(N)
    var_int.new_array_add = 0
    print("Mean (m):", mean)
    print("Amount of terms (N):", N)
    print("Array values for n:", var_int.progression)
    for n in var_int.progression:
      if n == N:
        var_int.new_array_add = mean * (1 + math.log(N))
        var_int.new_array.append(var_int.new_array_add)
      else:
        b = 1 + math.log(N, np.e) + (N - n) * math.log(N - n, np.e)
        c = (N - n + 1) * math.log(N - n + 1, np.e)
        var_int.new_array_add = mean * (b - c)
        var_int.new_array.append(var_int.new_array_add)
    print(var_int.new_array)

# + ========================================= +

# Random Interval Scheduling Generator

def rand_int(interval, amount): #()
  rand_int.amount = 4 # Amount of intervals (sec)
  rand_int.interval = interval # Length of each interval (sec)
  rand_int.prob = 1/rand_int.interval
  print('x')
  # Creating Array For within RI
  rand_int.new_array = []
  rand_int.progression = list(range(1, rand_int.interval, 1))
  rand_int.progression.append(rand_int.interval)
  # Creating Array For between RI
  rand_int.multiplier = list(range(1, rand_int.amount, 1))
  rand_int.multiplier.append(rand_int.amount)
  # Generating number
  print("Experiment length (sec):", rand_int.interval)
  print("Probability factor (prob/sec):", rand_int.prob)
  for rand_int.multiplier in range(rand_int.amount):
    for n in rand_int.progression:
        rand_int.random = np.random.uniform(0,1)
        if rand_int.random <= rand_int.prob:
            if rand_int.multiplier == 1:
              rand_int.new_array.append(n)
            else:
              interval_multiplier = n + (rand_int.interval * rand_int.multiplier)
              rand_int.new_array.append(interval_multiplier)
  print("Throughout the entire RI session of", (rand_int.amount*rand_int.interval),"(sec), RI trigger generated for:", rand_int.new_array, "sec")
