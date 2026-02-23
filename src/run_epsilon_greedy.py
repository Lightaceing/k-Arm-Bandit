import numpy as np
import random


#setting seed
random.seed(42)

from enviroment import create_enviroment
from bandit import take_attempts
from utils import plot_rewards, plot_epsilon_greedy_comparison
from agents import epsilon_greedy, exploit, explore



def select_randomly(env):
    select_arm = random.randint(1, len(env.keys()))
    return select_arm


new_env = create_enviroment(12)

attempt_count  = 500


tracking_list_epsilon, arm_chosen, _, current_value_epsilon = take_attempts(attempt_count, new_env, select_randomly, epsilon_greedy)
tracking_list_exploit, arm_chosen, _, current_value_exploit = take_attempts(attempt_count, new_env, select_randomly, exploit)
tracking_list_explore, arm_chosen, _, current_value_explore = take_attempts(attempt_count, new_env, select_randomly, explore)

all_scores = {
    "Epsilon Greedy" : current_value_epsilon, 
    "Exploit" : current_value_exploit, 
    "Explore" : current_value_explore, }



#print(tracking_list_epsilon)
plot_epsilon_greedy_comparison(all_scores)

#plot_rewards(tracking_list_epsilon, 'Epsilon greedy')
#print("Average Reward : ", sum(tracking_list)/attempt_count)
#print(tracking_list)
#reward_epsilon = sum(tracking_list)/attempt_count
#write_csv("epsilon_greedy", tracking_list)