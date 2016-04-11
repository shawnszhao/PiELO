from PyQt4 import QtCore, QtGui
import change_password, create_new_player, enter_score

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class GUIHandler(object):
    def __init__(self, QObject):
        self.object = QObject
        
    def setup_routes(self, q_object):
        QtCore.QObject.connect(self.object.CreateNewPlayer, QtCore.SIGNAL(_fromUtf8("accepted()")), create_new_player.main())
        QtCore.QObject.connect(self.object.CreateNewPlayer, QtCore.SIGNAL(_fromUtf8("accepted()")), q_object.accept)
        QtCore.QObject.connect(self.object.CreateNewPlayer, QtCore.SIGNAL(_fromUtf8("rejected()")), q_object.reject)

        QtCore.QObject.connect(self.object.ChangePassword, QtCore.SIGNAL(_fromUtf8("accepted()")), change_password.main())
        QtCore.QObject.connect(self.object.ChangePassword, QtCore.SIGNAL(_fromUtf8("accepted()")), q_object.accept)
        QtCore.QObject.connect(self.object.ChangePassword, QtCore.SIGNAL(_fromUtf8("rejected()")), q_object.reject)

        QtCore.QObject.connect(self.object.EnterScore, QtCore.SIGNAL(_fromUtf8("accepted()")), enter_score.main())
        QtCore.QObject.connect(self.object.EnterScore, QtCore.SIGNAL(_fromUtf8("accepted()")), q_object.accept)
        QtCore.QObject.connect(self.object.EnterScore, QtCore.SIGNAL(_fromUtf8("rejected()")), q_object.reject)

        # QtCore.QObject.connect(self.object.UnderTheHood, QtCore.SIGNAL(_fromUtf8("accepted()")), enter_score.main())
        # QtCore.QObject.connect(self.object.UnderTheHood, QtCore.SIGNAL(_fromUtf8("accepted()")), q_object.accept)
        # QtCore.QObject.connect(self.object.UnderTheHood, QtCore.SIGNAL(_fromUtf8("rejected()")), q_object.reject)

        QtCore.QMetaObject.connectSlotsByName(q_object)