from PyQt5 import QtCore, QtGui, QtWidgets

def setTheIcon(self, x, y, iconLink):
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(iconLink), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.btnBoard[x][y].setIcon(icon)

def setTheIconForBlack(self, x, y, iconLink):
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(iconLink), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.blackPieces[x][y].setIcon(icon)

def setTheIconForWhite(self, x, y, iconLink):
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(iconLink), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.whitePieces[x][y].setIcon(icon)