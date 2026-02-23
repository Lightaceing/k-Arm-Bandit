import random

from enviroment import create_enviroment
from bandit import take_attempts
from utils import plot_rewards, plot_epsilon_greedy_comparison
from agents import epsilon_greedy, exploit, explore

#setting seed
random.seed(42)



def select_randomly(env):
    select_arm = random.randint(1, len(env.keys()))
    return select_arm


new_env = create_enviroment(50)

attempt_count  = 5000

tracking_list_epsilon, arm_chosen, _, current_value_epsilon = take_attempts(attempt_count, new_env, select_randomly, epsilon_greedy)
tracking_list_exploit, arm_chosen, _, current_value_exploit = take_attempts(attempt_count, new_env, select_randomly, exploit)
tracking_list_explore, arm_chosen, _, current_value_explore = take_attempts(attempt_count, new_env, select_randomly, explore)

current_scores = {
        "Epsilon Greedy" : tracking_list_epsilon, 
    "Exploit" : tracking_list_exploit, 
    "Explore" : tracking_list_explore,
}

all_scores = {
    "Epsilon Greedy" : current_value_epsilon, 
    "Exploit" : current_value_exploit, 
    "Explore" : current_value_explore, }


plot_epsilon_greedy_comparison(current_scores, "Epsilon Greedy Comparison Graph", "Current Reward")
plot_epsilon_greedy_comparison(all_scores, "Current Run", "Average Rewards")
