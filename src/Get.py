from PyQt5 import QtCore, QtGui, QtWidgets
import chess

def getTheSquare(pos):
    if (pos == "A1"):
        return chess.A1
    elif (pos == "A2"):
        return chess.A2
    elif (pos == "A3"):
        return chess.A3
    elif (pos == "A4"):
        return chess.A4
    elif (pos == "A5"):
        return chess.A5
    elif (pos == "A6"):
        return chess.A6
    elif (pos == "A7"):
        return chess.A7
    elif (pos == "A8"):
        return chess.A8
    elif (pos == "B1"):
        return chess.B1
    elif (pos == "B2"):
        return chess.B2
    elif (pos == "B3"):
        return chess.B3
    elif (pos == "B4"):
        return chess.B4
    elif (pos == "B5"):
        return chess.B5
    elif (pos == "B6"):
        return chess.B6
    elif (pos == "B7"):
        return chess.B7
    elif (pos == "B8"):
        return chess.B8
    elif (pos == "C1"):
        return chess.C1
    elif (pos == "C2"):
        return chess.C2
    elif (pos == "C3"):
        return chess.C3
    elif (pos == "C4"):
        return chess.C4
    elif (pos == "C5"):
        return chess.C5
    elif (pos == "C6"):
        return chess.C6
    elif (pos == "C7"):
        return chess.C7
    elif (pos == "C8"):
        return chess.C8
    elif (pos == "D1"):
        return chess.D1
    elif (pos == "D2"):
        return chess.D2
    elif (pos == "D3"):
        return chess.D3
    elif (pos == "D4"):
        return chess.D4
    elif (pos == "D5"):
        return chess.D5
    elif (pos == "D6"):
        return chess.D6
    elif (pos == "D7"):
        return chess.D7
    elif (pos == "D8"):
        return chess.D8
    elif (pos == "E1"):
        return chess.E1
    elif (pos == "E2"):
        return chess.E2
    elif (pos == "E3"):
        return chess.E3
    elif (pos == "E4"):
        return chess.E4
    elif (pos == "E5"):
        return chess.E5
    elif (pos == "E6"):
        return chess.E6
    elif (pos == "E7"):
        return chess.E7
    elif (pos == "E8"):
        return chess.E8
    elif (pos == "F1"):
        return chess.F1
    elif (pos == "F2"):
        return chess.F2
    elif (pos == "F3"):
        return chess.F3
    elif (pos == "F4"):
        return chess.F4
    elif (pos == "F5"):
        return chess.F5
    elif (pos == "F6"):
        return chess.F6
    elif (pos == "F7"):
        return chess.F7
    elif (pos == "F8"):
        return chess.F8
    elif (pos == "G1"):
        return chess.G1
    elif (pos == "G2"):
        return chess.G2
    elif (pos == "G3"):
        return chess.G3
    elif (pos == "G4"):
        return chess.G4
    elif (pos == "G5"):
        return chess.G5
    elif (pos == "G6"):
        return chess.G6
    elif (pos == "G7"):
        return chess.G7
    elif (pos == "G8"):
        return chess.G8
    elif (pos == "H1"):
        return chess.H1
    elif (pos == "H2"):
        return chess.H2
    elif (pos == "H3"):
        return chess.H3
    elif (pos == "H4"):
        return chess.H4
    elif (pos == "H5"):
        return chess.H5
    elif (pos == "H6"):
        return chess.H6
    elif (pos == "H7"):
        return chess.H7
    elif (pos == "H8"):
        return chess.H8

def getTheIcon(self, x, y):
    currPos = "chess." + chr(65 + y) + str(8 - x)
    if(self.board.piece_at(getTheSquare(chr(65 + y) + str(8 - x)))):
        currPiece = self.board.piece_at(getTheSquare(chr(65 + y) + str(8 - x))).symbol()
    else:
        return ""
    print("curr: " + currPiece)
    if (currPiece == 'p'):
        return self.pawnBIconLink
    elif (currPiece == 'P'):
        return self.pawnWIconLink
    elif (currPiece == 'r'):
        return self.rookBIconLink
    elif (currPiece == 'R'):
        return self.rookWIconLink
    elif (currPiece == 'n'):
        return self.knightBIconLink
    elif (currPiece == 'N'):
        return self.knightWIconLink
    elif (currPiece == 'b'):
        return self.bishopBIconLink
    elif (currPiece == 'B'):
        return self.bishopWIconLink
    elif (currPiece == 'q'):
        return self.queenBIconLink
    elif (currPiece == 'Q'):
        return self.queenWIconLink
    elif (currPiece == 'k'):
        return self.kingBIconLink
    elif (currPiece == 'K'):
        return self.kingWIconLink
    else:
        return ""
