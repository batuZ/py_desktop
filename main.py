import sys

from PyQt5.Qt import *
from PyQt5.uic import loadUi

from ui.root_custom import Root
from ui.sub_view_custom import SubView
from ui.custom_view import CustomView

from ui.FixWindow import FixWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 加载全局静态样式
    with open('./ui/qss.css', 'r', encoding='UTF-8') as f:
        app.setStyleSheet(f.read())




    """
    # 单窗体，多界面切换模式
    # fix = loadUi('ui/Fix-window.ui') # 直接从ui获取对象
    fix = FixWindow()
    fix.show()

   
    # 继承designer创建的form类，方便在designer中修改，程序中更新
    root_view = Root()
    root_view.show()

    # 直接加载uiy文件，不转py
    sub_view = SubView()
    sub_view.show()
    """

    # 不用designer，手撸UI
    custom_view = CustomView()
    custom_view.show()


    sys.exit(app.exec_())
