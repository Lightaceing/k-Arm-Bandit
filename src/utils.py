import numpy as np
import matplotlib.pyplot as plt
import datetime

import csv

#Plot Epsilon-greedy comparison
def plot_epsilon_greedy_comparison(reward_lists, graph_title, y_label):
    
    fig, ax = plt.subplots()

    for title, score in reward_lists.items():
        ax.plot(score, label=str(title))
    
    ax.set_ylabel(y_label)
    ax.set_xlabel("Steps")
    ax.set_title(graph_title)
    ax.legend()


    plt.show()

def plot_rewards(reward_list, title):

    fig, ax = plt.subplots()

    scores = np.asarray(reward_list)
    ax.plot(scores)
    ax.set_ylabel("Rewards")
    ax.set_xlabel("Steps")
    ax.set_title(title)
    plt.show()


def write_csv(filename, data):

    #File path
    csv_file_path = "results/"+filename+"_"+str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))+'.csv'

    #Data prep



    #Data writing
    with open(csv_file_path, mode='w', newline='') as file:
        # Create a csv.writer object
        writer = csv.writer(file)
        writer.writerows([[x] for x in data])