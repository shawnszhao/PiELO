from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


class ChangePasswordHandler(object):
    def __init__(self, QObject):
        self.object = QObject
        
    def setup_routes(self, q_object):
        QtCore.QObject.connect(self.object.Okay, QtCore.SIGNAL(_fromUtf8("accepted()")), self.okay)
        QtCore.QObject.connect(self.object.Okay, QtCore.SIGNAL(_fromUtf8("accepted()")), q_object.accept)
        QtCore.QObject.connect(self.object.Okay, QtCore.SIGNAL(_fromUtf8("rejected()")), q_object.reject)

    def okay(self):
        username = self.object.username.displayText()
        oldpass = self.object.oldpass.displayText()
        newpass = self.object.newpass.displayText()
        newpassconf = self.object.newpassconf.displayText()
        print(username)
        print(oldpass)
        print(newpass)
        print(newpassconf)