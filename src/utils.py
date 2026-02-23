import numpy as np
import matplotlib.pyplot as plt
import csv
import datetime


#Plot Epsilon-greedy comparison
def plot_epsilon_greedy_comparison(reward_lists):
    fig, ax = plt.subplots()


    for title, score in reward_lists.items():
        ax.plot(score, label=str(title))
    ax.set_ylabel("Rewards")
    ax.set_xlabel("Steps")
    ax.set_title("Epsilon Greedy Comparison Graph")
    ax.legend()
    plt.show()

def plot_rewards(reward_list, figsize = (1, 1)):
    scores = np.asarray(reward_list)
    plt.plot(scores)
    plt.ylabel("Rewards")
    plt.xlabel("Steps")
    plt.title("EMPTY PASS")
    plt.figure(figsize = figsize)
    plt.show()



def write_csv(filename, data):
    csv_file_path = "results/"+filename+"_"+str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))+'.csv'
    with open(csv_file_path, mode='w', newline='') as file:
        # Create a csv.writer object
        writer = csv.writer(file)
        writer.writerows([[x] for x in data])