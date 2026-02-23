import random

def calculate_average_value(estimate_values, arm_selected, current_value, i):
    new_value = estimate_values[arm_selected] + (1/(i+1)) * (current_value - estimate_values[arm_selected])
    return new_value


def take_attempts(attempts, enviroment_details, select_randomly, arm_selection_tech):
    #Init. all estimates to 0
    estimate_values = {}
    for i in range(0, len(enviroment_details.keys())): #Range over no. of arms
        estimate_values[i] = 0

    cummulative_reward = [0]
    selected_arm_list = []
    tracking_list = []

    for i in range(0, attempts):
        select_val = random.randint(0, 9)#accessing 0-9 total 10 points #TODO: needs to replaced by size
        
        #Selecting technique to be used for selection
        arm_selected = arm_selection_tech(enviroment_details, estimate_values, epsilon = 0 ) #range from 0 to no. of arms - 1
        selected_arm_list.append(arm_selected)

        #Obtain Value
        current_value = enviroment_details[arm_selected][select_val]
        if (i%100 == 0):
            tracking_list.append(current_value)
        estimate_values[arm_selected] = calculate_average_value(estimate_values, arm_selected, current_value, i)
        cummulative_reward.append(current_value+cummulative_reward[-1])

    return tracking_list, selected_arm_list, estimate_values, cummulative_reward


