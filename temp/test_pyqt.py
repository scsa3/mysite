import sys
import threading

from PyQt5 import QtGui, QtWidgets


def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    b = QtWidgets.QLabel(w)
    b.setText("Hello World!")
    w.setGeometry(100, 100, 200, 50)
    b.move(50, 20)
    w.setWindowTitle("PyQt")
    w.show()
    sys.exit(app.exec_())


def my_qt():
    window()
    print('qt done')


def some_view():
    t = threading.Thread(target=my_qt)
    t.start()
    print('view done')

some_view()
