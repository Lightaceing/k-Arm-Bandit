import random
import numpy as np


def create_enviroment(n_arms : int, max_mean = 10):
    """
    Input : n_arms -> no. of arms
          : max_mean -> sets the mean range from 0 to max_mean || by default set to 10
    Output : k_mean_dict -> Dictonary with key values as integer : normal distr. vals
    
    """
    #assertions
    assert n_arms > 0 , f"n_arms needs to be an integer larger than 0 NOT {n_arms}"
    assert max_mean, f"max_mean needs to be an integer NOT {max_mean}" 
    
    k_mean_dict = {}
    keys = list(range(1, n_arms+1))
    values = []
    for i in range(n_arms):#loc needs to be random a bit
        rand_val = random.randint(0, max_mean)#range b/w 0 to 10
        curr_val = np.random.normal(loc = rand_val, scale = 1, size = 10)#normal dist. #size->no. of observations
        values.append(curr_val)
        #filling dict
    k_mean_dict = dict(zip(keys, values))
    return k_mean_dict

