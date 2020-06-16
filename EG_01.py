#!/usl/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/24 15:53
# @Author  : X 浩

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon

class EG_O1(QMainWindow):
    def __init__(self, parent=None):
        super(EG_O1, self).__init__(parent)

        self.setWindowTitle('第一个主窗口应用')

        self.resize(400, 300)
        self.status = self.statusBar()
        self.status.showMessage('只存在五秒内的消息', 1000)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    app.setWindowIcon(QIcon('D:\hhh.jpg'))
    EG_O1 = EG_O1()
    EG_O1.show()

    sys.exit(app.exec_()) # 阿萨大时代撒旦asda