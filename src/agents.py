import random
import numpy as np

#Implementation of Epsilon Greedy Agent

def epsilon_greedy(enviroment, current_estimate, epsilon = 0.2):
    random_val = random.randint(1,100)
    if(random_val <= epsilon*100):
        epsilon_greedy_arm = explore(current_estimate, enviroment)
    else:
        epsilon_greedy_arm = exploit(enviroment, current_estimate, epsilon = 0)
    return epsilon_greedy_arm

#Implementation of Exploitation Agent
def exploit(enviroment, current_estimate, epsilon = 0):
    #Will always select the first one as all are 0
    greedy_arm = max(current_estimate, key=lambda k: current_estimate[k])
    return greedy_arm


#Implementation of Exploring Agent
def explore(enviroment, current_estimate, epsilon = 0):
    select_arm = random.randint(0, len(enviroment.keys())-1)#Arms from 0 to n-1
    return select_arm


