import random
import numpy as np


def create_enviroment(n_arms : int, max_mean = 10, size = 10):
    """
    Input : n_arms -> no. of arms
          : max_mean -> sets the mean range from 0 to max_mean || by default set to 10
          : size -> no. of different values that can be taken from each arm
    Output : k_mean_dict -> Dictonary with key values as integer : normal distr. vals
    
    """
    #assertions
    assert n_arms > 0 , f"n_arms needs to be an integer larger than 0 NOT {n_arms}"
    assert max_mean, f"max_mean needs to be an integer NOT {max_mean}" 
    
    k_mean_dict = {}

    keys = list(range(0, n_arms))
    
    values = []
    
    for _ in range(n_arms):#loc needs to be random a bit
        rand_val = random.randint(0, max_mean)#range b/w 0 to 10
        curr_val = np.random.normal(0, 1, size = size)#normal dist. #size->no. of observations
        values.append(curr_val)
        
    k_mean_dict = dict(zip(keys, values))
    return k_mean_dict

