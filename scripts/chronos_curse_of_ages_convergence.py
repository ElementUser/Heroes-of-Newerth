"""
This script returns the number of successful procs of Chronos' Curse of Ages, given a number of iterations.
The script was primarily created to simulate the convergence of Curse of Ages procs as the number of iterations approaches infinity to empirically determine the "true RNG" value of the skill.
"""

from __future__ import division
import random

def chance(counter):
    """
    Definition for the chance() function
    """
    if counter >= 5: return 1
    else:
        counter_temporary = counter * 14
        roll = random.randint(0,100)
        if roll < counter_temporary: return 1
  
# Test iterations
counter = 0
success = 0
maxIterations = 1000000

for i in range(maxIterations):
    result = chance(counter)
    if result == 1:
        counter = 0
        success += 1
    else: counter += 1


print(f'The Total number of iterations is {maxIterations}.\nThe number of successes is {success}\nThe success rate is {success/maxIterations}')
