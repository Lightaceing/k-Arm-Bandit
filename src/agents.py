import random

#Implementation of Epsilon Greedy Agent

def epsilon_greedy(env, known_vals, epsilon = 0.2):
    random_val = random.randint(1,100)
    if(random_val <= epsilon*100):
        arm = explore(known_vals, env)
        print('')
    else:
        arm = exploit(known_vals)
    return arm

#Implementation of Exploitation Agent
def exploit(known_vals, env = 1, epsilon = 0):
    greedy_arm = max(known_vals)
    return greedy_arm


#Implementation of Exploring Agent
def explore(known_vals, env, epsilon = 0):
    val = max(known_vals)
    select_arm = val
    while (select_arm == val):
        select_arm = random.randint(1, len(env.keys()))
    return select_arm


