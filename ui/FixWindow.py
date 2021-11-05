from PyQt5.Qt import *
from PyQt5.uic import loadUi


class FixWindow(QWidget):
    def __init__(self, parent=None):
        super(FixWindow, self).__init__()
        # 把唤出自己的对象拿好
        self.father = parent
        loadUi('ui/Fix-window.ui', self)
        self.fix1 = loadUi('ui/Fix-window1.ui')

    def backBtn_click(self):
        print('backBtn_click')
        self.clearUi()

    def goBtn_click(self):
        self.ui = loadUi('ui/Fix-window1.ui', self)

    def clearUi(self):
        print(self.children())
