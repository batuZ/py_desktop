from PyQt5.Qt import QWidget
from PyQt5.uic import loadUi


class SubView(QWidget):

    def __init__(self, parent=None):
        super().__init__()
        # 把唤出自己的对象拿好
        self.father = parent
        loadUi('ui/sub_view.ui', self)
        self.pushButton.clicked.connect(self.send_msg_to_parent)

    def send_msg_to_parent(self):
        # 判断一下有没有召唤者，避免调用空对象
        self.father.callback('send_msg_to_parent') if self.father else print('send_msg_to_parent')

    def pushBtn2_clicked(self):
        '''这个信号是在PyDesigner里定义的'''
        print(123)
