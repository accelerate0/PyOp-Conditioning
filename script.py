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
def var_int(N, m):
    var_int.new_array = []
    var_int.progression = list(range(1, N, 1))
    var_int.progression.append(N)
    var_int.new_array_add = 0
    print("Mean (m):", m)
    print("Amount of terms (N):", N)
    print("Array values for n:", var_int.progression)
    for n in var_int.progression:
      if n == N:
        var_int.new_array_add = m * (1 + math.log(N))
        var_int.new_array.append(var_int.new_array_add)
      else:
        b = 1 + math.log(N, np.e) + (N - n) * math.log(N - n, np.e)
        c = (N - n + 1) * math.log(N - n + 1, np.e)
        var_int.new_array_add = m * (b - c)
        var_int.new_array.append(var_int.new_array_add)
    print(var_int.new_array)

# + ========================================= +


def rand_int(N, t): #()
    rand_int.mri = 0
    rand_int.t =
    rand_int.p =
    rand_int.new_array_add = 0
    print("Mean (m):", m)
    print("Amount of terms (N):", N)
    print("Array values for n:", var_int.progression)
    for n in var_int.progression:
      if n == N:
        var_int.new_array_add = m * (1 + math.log(N))
        var_int.new_array.append(var_int.new_array_add)
      else:
        b = 1 + math.log(N, np.e) + (N - n) * math.log(N - n, np.e)
        c = (N - n + 1) * math.log(N - n + 1, np.e)
        var_int.new_array_add = m * (b - c)
        var_int.new_array.append(var_int.new_array_add)
    print(var_int.new_array)
