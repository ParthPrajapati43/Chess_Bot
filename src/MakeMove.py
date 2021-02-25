from PyQt5 import QtCore, QtGui, QtWidgets
import chess

def makeMove(self, posNum, posAlpha): 
    # print(str(8 - posNum) + chr(97 + posAlpha) + " clicked!")
    if (not self.pieceSelected and self.selectedPiece == ""):
        self.pieceSelected = True
        self.selectedPiece = str(8 - posNum) + chr(97 + posAlpha)
        self.btnBoard[posNum][posAlpha].setStyleSheet("background: yellow;\n"
            "color: white;\n"
            "height: 65px;\n"
            "width: 65px;\n"
            "icon-size: 65px;\n"
            "")
        for i in range(8):
            for j in range(8):
                if(self.selectedPiece != (str(8 - i) + chr(97 + j))):
                    if (chess.Move.from_uci(self.selectedPiece[::-1] + chr(97 + j) + str(8 - i)) in self.board.legal_moves):
                        self.legalMoves.append(self.selectedPiece + str(8 - i) + chr(97 + j))
                        self.btnBoard[i][j].setStyleSheet("background: yellow;\n"
                            "color: white;\n"
                            "height: 65px;\n"
                            "width: 65px;\n"
                            "icon-size: 65px;\n"
                            "")

    elif(self.selectedPiece == (str(8 - posNum) + chr(97 + posAlpha))):
        self.pieceSelected = False
        self.selectedPiece = ""
        for i in range(8):
            for j in range(8):
                if((i+j)%2 == 0):
                    self.btnBoard[i][j].setStyleSheet("background: rgb(118, 150, 86);\n"
                        "color: white;\n"
                        "height: 65px;\n"
                        "width: 65px;\n"
                        "icon-size: 65px;\n"
                        "")
                else:
                    self.btnBoard[i][j].setStyleSheet("background: white;\n"
                    "color: black;\n"
                    "height: 65px;\n"
                    "width: 65px;\n"
                    "icon-size: 65px;\n"
                    "")
    elif ((self.selectedPiece + str(8 - posNum) + chr(97 + posAlpha)) in self.legalMoves):
        if (self.getTheIcon(posNum, posAlpha) != ""):
            if (self.turnOfWhite):
                self.setTheIconForBlack(self.blackOut // 8, self.blackOut % 8, self.getTheIcon(posNum, posAlpha))
                self.blackOut += 1
            else:
                self.setTheIconForWhite(self.whiteOut // 8, self.whiteOut % 8, self.getTheIcon(posNum, posAlpha))
                self.whiteOut += 1
        self.setTheIcon(posNum, posAlpha, self.getTheIcon(8-(ord(self.selectedPiece[0])-48), ord(self.selectedPiece[1])-97))
        self.setTheIcon(8 - (ord(self.selectedPiece[0]) - 48), ord(self.selectedPiece[1]) - 97, "")
        self.board.push(chess.Move.from_uci(self.selectedPiece[::-1] + chr(97 + posAlpha) + str(8 - posNum)))
        self.pieceSelected = False
        self.selectedPiece = ""
        self.turnOfWhite = not self.turnOfWhite
        for i in range(8):
            for j in range(8):
                if((i+j)%2 == 0):
                    self.btnBoard[i][j].setStyleSheet("background: rgb(118, 150, 86);\n"
                        "color: white;\n"
                        "height: 65px;\n"
                        "width: 65px;\n"
                        "icon-size: 65px;\n"
                        "")
                else:
                    self.btnBoard[i][j].setStyleSheet("background: white;\n"
                    "color: black;\n"
                    "height: 65px;\n"
                    "width: 65px;\n"
                    "icon-size: 65px;\n"
                    "")
    