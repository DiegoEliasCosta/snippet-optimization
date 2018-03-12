import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("PyQt Tuts!")
        self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))

        extractAction = QtGui.QAction("&Exit", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip("Leave the App")
        extractAction.triggered.connect(self.close_application)
        self.statusBar()

        #For people who are using Ubuntu, the menuBar doesn't appear
        # because it's a feature of Ubuntu's Unity shell called global menu bar.
        # #So, if you want your menu to take its place on top of a window regardless
        # of graphical shell preferences, you should use Qt menu bar instead of native one:

        mainMenu = QtGui.QMenuBar()
        mainMenu.setNativeMenuBar(False)
        self.setMenuBar(mainMenu)

        fileMenu = mainMenu.addMenu('File')
        fileMenu.addAction(extractAction)

        self.home()

    def home(self):
        btn = QtGui.QPushButton("Quit", self)
        btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        btn.move(400, 250)

        extractAction = QtGui.QAction(QtGui.QIcon)


        self.show()

    def close_application(self):
        sys.exit()


def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()