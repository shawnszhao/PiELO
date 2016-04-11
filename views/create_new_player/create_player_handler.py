import pickle
from PyQt4 import QtCore, QtGui
import datetime
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

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


class CreatePlayerHandler(object):
    def __init__(self, QObject):
        self.object = QObject
        
    def setup_routes(self, q_object):
        QtCore.QObject.connect(self.object.Okay, QtCore.SIGNAL(_fromUtf8("accepted()")), self.okay)
        QtCore.QObject.connect(self.object.Okay, QtCore.SIGNAL(_fromUtf8("accepted()")), q_object.accept)
        QtCore.QObject.connect(self.object.Okay, QtCore.SIGNAL(_fromUtf8("rejected()")), q_object.reject)
        QtCore.QMetaObject.connectSlotsByName(q_object)

    def okay(self):
        pkl_file = open('/etc/PiELO/AllSammys.pkl', 'rb')
        AllSammys = pickle.load(pkl_file)
        a=self.object.NameEntryBox.text()
        self.object.NameEntryBox.setText('')
        player1 = a.replace(" ", "")
        exec("%s = Sammy(a)" % (a.replace(" ","")))
        AllSammys.append(a)
        output = open('AllSammys' + '.pkl', 'wb')
        pickle.dump(AllSammys, output)        
        output1 = open(player1 + '.pkl','wb')
        pickle.dump(player1, output1)    
        print(a)
        