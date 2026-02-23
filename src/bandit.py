import random

#basic chosing system
def take_attempts(attempts, env, selection_fn, arm_selection_tech):
    """
    Input :     attempts                     | no of attempts
                env                          | enviroment
                selection_fn                 | fn using which arm is selected
                arm_selection_tech           | technique used to select arms
                
    Output :    tracking_list                | list containing all the rewards
                arm_chosen                   | arm chosen
                known_vals                   | arm : total reward
    """
    
    known_vals = {}
    for i in range(0, len(env.keys())):
        known_vals[i] = 0
        
    select_arms = []
    vals = []
    tracking_list = []
    cummulative_reward = [0]

    for i in range(1, attempts):
        #pulling from a random distribution
        select_val = random.randint(0, 9)#accessing 0-9 total 10 points
        #selecting arm
        #arm = explore(known_vals)
        
        #Selecting technique
        select_arm = arm_selection_tech(known_vals, env, 0.2)#n_arms
        
        current_value = env[select_arm][select_val]
        tracking_list.append(current_value)#save in a list
        
        select_arms.append(select_arm)
        vals.append(current_value)      
        
        known_vals = dict(zip(select_arms, vals))
        #print(select_arm, known_vals)

        cummulative_reward.append(current_value+cummulative_reward[-1])
    total_reward = sum(tracking_list)
    
    return tracking_list, select_arms, known_vals, cummulative_reward