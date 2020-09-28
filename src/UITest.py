from PySide2 import QtWidgets

from UI import main

class GameBoard(main.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(GameBoard, self).__init__()
        self.setupUi(self)
        self.deactivateAll()
        self.btnNewGame.clicked.connect(self.newGame)
        self.btnRollDice.clicked.connect(self.diceRolled)
        self.btnWhite1.clicked.connect(self.movement)

    def deactivateAll(self):
        self.btnBlack1.setEnabled(False)
        self.btnBlack2.setEnabled(False)
        self.btnBlack3.setEnabled(False)
        self.btnBlack4.setEnabled(False)
        self.btnBlack5.setEnabled(False)
        self.btnBlack6.setEnabled(False)
        self.btnBlack7.setEnabled(False)

        self.btn00.setEnabled(False)
        self.btn01.setEnabled(False)
        self.btn02.setEnabled(False)
        self.btn03.setEnabled(False)
        self.btn06.setEnabled(False)
        self.btn07.setEnabled(False)

        self.btn10.setEnabled(False)
        self.btn11.setEnabled(False)
        self.btn12.setEnabled(False)
        self.btn13.setEnabled(False)
        self.btn14.setEnabled(False)
        self.btn15.setEnabled(False)
        self.btn16.setEnabled(False)
        self.btn17.setEnabled(False)

        self.btn20.setEnabled(False)
        self.btn21.setEnabled(False)
        self.btn22.setEnabled(False)
        self.btn23.setEnabled(False)
        self.btn26.setEnabled(False)
        self.btn27.setEnabled(False)

        self.btnWhite1.setEnabled(False)
        self.btnWhite2.setEnabled(False)
        self.btnWhite3.setEnabled(False)
        self.btnWhite4.setEnabled(False)
        self.btnWhite5.setEnabled(False)
        self.btnWhite6.setEnabled(False)
        self.btnWhite7.setEnabled(False)

        self.btnRollDice.setEnabled(False)
        self.lblDice1.setText("0")
        self.lblDice2.setText("0")
        self.lblDice3.setText("0")

    def newGame(self):
        self.btnRollDice.setEnabled(True)
        self.lblDice1.setText("0")
        self.lblDice2.setText("0")
        self.lblDice3.setText("0")

        self.btn00.setEnabled(False)
        self.btn01.setEnabled(False)
        self.btn02.setEnabled(False)
        self.btn03.setEnabled(False)
        self.btn06.setEnabled(False)
        self.btn07.setEnabled(False)

        self.btn10.setEnabled(False)
        self.btn11.setEnabled(False)
        self.btn12.setEnabled(False)
        self.btn13.setEnabled(False)
        self.btn14.setEnabled(False)
        self.btn15.setEnabled(False)
        self.btn16.setEnabled(False)
        self.btn17.setEnabled(False)

        self.btn20.setEnabled(False)
        self.btn21.setEnabled(False)
        self.btn22.setEnabled(False)
        self.btn23.setEnabled(False)
        self.btn26.setEnabled(False)
        self.btn27.setEnabled(False)

        self.btnWhite1.setEnabled(False)
        self.btnWhite2.setEnabled(False)
        self.btnWhite3.setEnabled(False)
        self.btnWhite4.setEnabled(False)
        self.btnWhite5.setEnabled(False)
        self.btnWhite6.setEnabled(False)
        self.btnWhite7.setEnabled(False)

    def diceRolled(self):
        self.btnRollDice.setEnabled(False)

        self.btnWhite1.setEnabled(True)
        self.btnWhite2.setEnabled(True)
        self.btnWhite3.setEnabled(True)
        self.btnWhite4.setEnabled(True)
        self.btnWhite5.setEnabled(True)
        self.btnWhite6.setEnabled(True)
        self.btnWhite7.setEnabled(True)

        self.lblDice1.setText("Dado1")
        self.lblDice2.setText("Dado2")
        self.lblDice3.setText("Dado3")

    def movement(self):
        self.btn10.setEnabled(True)
        self.btn11.setEnabled(True)
        self.btn12.setEnabled(True)
        self.btn13.setEnabled(True)
        self.btn14.setEnabled(True)
        self.btn15.setEnabled(True)
        self.btn16.setEnabled(True)
        self.btn17.setEnabled(True)

        self.btn20.setEnabled(True)
        self.btn21.setEnabled(True)
        self.btn22.setEnabled(True)
        self.btn23.setEnabled(True)
        self.btn26.setEnabled(True)
        self.btn27.setEnabled(True)

        self.btn23.setStyleSheet(u"background-color: rgba(255, 0, 0, 50);")









if __name__=='__main__':
    app = QtWidgets.QApplication()
    qt_app = GameBoard()
    qt_app.show()
    app.exec_()
