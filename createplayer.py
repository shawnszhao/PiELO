
# coding: utf-8

# This function is to be used with the "create a new player" GUI.
# 
# This will be written in the form of a function that takes one input (name), creates an instance of the class Sammy, and then saving that instance to the corresponding pickle file. 

# In[ ]:

import numpy as np
import pickle
import datetime
from numpy import pi, sqrt, linspace


# In[ ]:

class Sammy:
    """ The class Sammy will contain the information about each player, containing the following attributes: 
    
    Attributes: 
        Name: A string representing the Sammy's name. This is the only input, and must be a string.
        Password: A password to be entered by each player so no false games can be recorded. Defaults to string "password".
        ELO: A list containing their ELO scores. Everyone starts at 1500
        Sinks: A list containing the number of sinks per game
        Score: A list containing the score of each game
        Opponent Name: A list of names to ensure no false names are created to inflate or deflate ELOs. 
        Opponent Rank: A list containing the ELO of the opponent of each game
    """
    def __init__(self, name):
        self.name = name
        self.password = 'password'
        self.ELO = [1500]
        self.sinks = []
        self.score = []
        self.oppname = []
        self.opprank = []
        self.date = [str(datetime.date.today())]


# In[ ]:

"""
Loads list of AllSammys
"""
import pickle
pkl_file = open('AllSammys.pkl', 'rb')
AllSammys = pickle.load(pkl_file)


# In[ ]:

def createaplayer(name):
    exec("%s = Sammy(name)" % (name.replace(" ","")))
    AllSammys.append(name)
    output = open('AllSammys' + '.pkl', 'wb')
    pickle.dump(AllSammys, output)

def accept(**kwargs):
    print('Accepted bitch')
    from IPython import embed
    embed()
    return False

