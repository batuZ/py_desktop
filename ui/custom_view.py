from PyQt5.Qt import *


class CustomView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("控件")
        self.resize(200, 200)
