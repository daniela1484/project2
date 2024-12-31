# -*- coding: utf-8 -*-
"""project2.ipynb
"""

days = "SSRNRNSSSSSSNRSNSSRNSRNSSSNSRRRNSSSNRRSSSSNRSSNSRRRRRRNSSSSSRRRSNSNRRRRSRSRNSNSRRNRRNRSSNSRNRNSSRRSRNSSSNRSRRSSNRSNRRNSSSSNSSNSRSRRNSSNSSRNSSRRNRRRSRNRRRNSSSNRNSRNSNRNRSSSRSSNRSSSNSSSSSSNSSSNSNSRRNRNRRRRSRRRSSSSNRRSSSSRSRRRNRRRSSSSRRNRRRSRSSRRRRSSRNRRRRRRNSSRNRSSSNRNSNRRRRNRRRNRSNRRNSRRSNRRRRSSSRNRRRNSNSSSSSRRRRSRNRSSRRRRSSSRRRNRNRRRSRSRNSNSSRRRRRNSNRNSNRRNRRRRRRSSSNRSSRSNRSSSNSNRNSNSSSNRRSRRRNRRRRNRNRSSSNSRSNRNRRSNRRNSRSSSRNSRRSSNSRRRNRRSNRRNSSSSSNRNSSSSSSSNRNSRRRNSSRRRNSSSNRRSRNSSRRNRRNRSNRRRR "

# Initialize counters for 'SS', 'SR', 'SN', 'RR', 'RS', 'RN', 'NR', and 'NS'.
count_SS = 0
count_SR = 0
count_SN = 0
count_RR = 0
count_RS = 0
count_RN = 0
count_NR = 0
count_NS = 0

j = 0
# Loop through the string and check for pairs
for i in range(0, len(days)):
  j = j + 1
  pair = days[i:i+2]
  if pair == "SS":
    count_SS += 1
  elif pair == "SR":
    count_SR += 1
  elif pair == "SN":
    count_SN += 1
  elif pair == "RR":
    count_RR += 1
  elif pair == "RS":
    count_RS += 1
  elif pair == "RN":
    count_RN += 1
  elif pair == "NR":
    count_NR += 1
  elif pair == "NS":
    count_NS += 1
  else:
    print(pair)
    print(i)

# Print
print(f"SS count: {count_SS}")
print(f"SR count: {count_SR}")
print(f"SN count: {count_SN}")
print(f"RR count: {count_RR}")
print(f"RS count: {count_RS}")
print(f"RN count: {count_RN}")
print(f"NR count: {count_NR}")
print(f"NS count: {count_NS}")


# Libraries needed
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# Define the transition matrix
P = np.array([[0, 0.528846, 0.4711538],
              [0.2794118, 0.495098, 0.2254902],
              [0.2460733, 0.256545, 0.4973822]], dtype=np.float64)

# Calculate the stationary distribution
# We solve πP = π, which can be rewritten as π(P.T - I) = 0,
# where I is the identity matrix
# We add a constraint that the sum of π must be 1

# Create the augmented matrix for the system
n = P.shape[0]
A = np.vstack((P.T - np.eye(n), np.ones(n)))
b = np.zeros(n + 1)
b[-1] = 1  # The sum of the probabilities should be 1

# Solve the system using least squares
solution = np.linalg.lstsq(A, b, rcond=None)[0]

# The solution gives us the stationary distribution
print("Stationary distribution:", solution)
