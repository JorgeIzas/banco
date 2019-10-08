from PyQt5.QtWidgets import QApplication, QMainWindow
from untitled import Ui_mainWindow

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())