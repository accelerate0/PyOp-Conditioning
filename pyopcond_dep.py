import numpy as np
import math
import random

# + ========================================= +
# +++ Variable Interval Scheduling Generator +++
#
#       Utilizes the Hoffman-Fleshler Constant Probability Distribution
#       Based on Hantula (1991) and Fleshler et Hoffman (1962)
#       Program Parameters
#           N = Amount of terms
#           m = mean
#           n = the nth term of progression

def var_int(N, mean):
    # Declaring Variables
    var_int.mean = mean
    var_int.N = N
    var_int.new_array = []
    # Creating Output Array
    var_int.progression = list(range(1, var_int.N, 1))
    var_int.progression.append(N)
    var_int.new_array_add = 0
    print("Mean (m):", var_int.mean)
    print("Amount of terms (N):", var_int.N)
    print("Array values for n:", var_int.progression)
    for var_int.n in var_int.progression:
      if var_int.n == var_int.N:
        var_int.new_array_add = var_int.mean * (1 + math.log(N))
        var_int.new_array.append(var_int.new_array_add)
      else:
        var_int.b = 1 + math.log(var_int.N, np.e) + (var_int.N - n) * math.log(var_int.N - var_int.n, np.e)
        var_int.c = (var_int.N - var_int.n + 1) * math.log(var_int.N - var_int.n + 1, np.e)
        var_int.new_array_add = var_int.mean * (var_int.b - var_int.c)
        var_int.new_array.append(var_int.new_array_add)
    var_int.output_random = random.shuffle(var_int.new_array)
    var_int.output_straight = var_int.new_array

# + ========================================= +
# +++ Random Interval Scheduling Generator +++
#
#       Based on Millenson (1963) and Bancroft et Bourrett (2008)

def rand_int(interval, amount): #()
    # Declaring Variables
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
        for rand_int.n in rand_int.progression:
            rand_int.random = np.random.uniform(0,1)
            if rand_int.random <= rand_int.prob:
                if rand_int.multiplier == 1:
                  rand_int.new_array.append(rand_int.n)
                else:
                  rand_int.interval_multiplier = rand_int.n + (rand_int.interval * rand_int.multiplier)
                  rand_int.new_array.append(rand_int.interval_multiplier)
    rand_int.output = rand_int.new_array

# + ========================================= +
# +++ Variable Ratio Scheduling Generator +++
#
#

def var_ratio(amount, min, max): #()
    # Declaring Variables
    var_ratio.amount = amount # Amount of total rewards (sec)
    var_ratio.min = min # Minimum amount of inputs (ie lever presses)
    var_ratio.max = max  # Maximum amount of inputs (ie lever presses)
    # Creating Output Array
    var_ratio.new_array = []
    var_ratio.progression = list(range(1, var_ratio.amount, 1))
    var_ratio.progression.append(var_ratio.amount)
    for var_ratio.n in range(var_ratio.progression):
        random.randrange(var_ratio.min, 1 + var_ratio.max, 1)
        var_ratio.new_array.append(var_ratio.n)
    var_ratio.output = var_ratio.new_array

# + ========================================= +
# +++ Random Ratio Scheduling Generator +++
#
#
def rand_ratio(interval, mean): #()
    # Declaring Variables
    rand_ratio.mean = 4 # Amount of intervals (sec)
    rand_ratio.interval = interval # Length of each interval (sec)
    rand_ratio.prob = 1/rand_ratio.interval
    print('x')
    # Creating Array For within RI
    rand_ratio.new_array = []
    rand_ratio.progression = list(range(1, rand_ratio.interval, 1))
    rand_ratio.progression.append(rand_ratio.interval)
    # Creating Array For between RI
    rand_ratio.multiplier = list(range(1, rand_ratio.amount, 1))
    rand_ratio.multiplier.append(rand_ratio.amount)
    # Generating number
    print("Experiment length (sec):", rand_ratio.interval)
    print("Probability factor (prob/sec):", rand_ratio.prob)
    for rand_ratio.multiplier in range(rand_ratio.amount):
        for rand_ratio.n in rand_ratio.progression:
            rand_ratio.random = np.random.uniform(0,1)
            if rand_ratio.random <= rand_ratio.prob:
                if rand_ratio.multiplier == 1:
                  rand_ratio.new_array.append(rand_ratio.n)
                else:
                  rand_ratio.interval_multiplier = rand_ratio.n + (rand_ratio.interval * rand_ratio.multiplier)
                  rand_ratio.new_array.append(rand_ratio.interval_multiplier)
    rand_int.output = rand_int.new_array







# ======= #
