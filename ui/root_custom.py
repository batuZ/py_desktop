from PyQt5.Qt import *
from ui.root import Ui_Root_Form
from ui.sub_view_custom import SubView


class Root(QMainWindow, Ui_Root_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.Sub_Form1 在designer里设置了事件和响应动作
        # self.Sub_Form2 用来演示弹出新窗口并传参，同时接收新窗口回调
        # self.Sub_Form3 手动定义内部事件和响应函数
        self.btn3.clicked.connect(self.btn_clicked)
        self.new_window_btn.clicked.connect(self.show_new)
        self.sub_view = SubView(self)

    def btn_clicked(self):
        self.label.setText('btn3 clicked!!')

    def callback(self, str1):
        self.label.setText(str1)

    def show_new(self):
        """ 模态弹出子窗口 """
        self.sub_view.setWindowModality(Qt.ApplicationModal)
        self.sub_view.show()
