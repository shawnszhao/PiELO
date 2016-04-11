from views import main

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


if __name__ == '__main__':
	main()