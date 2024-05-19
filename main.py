from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLineEdit, QVBoxLayout, QMessageBox, QHBoxLayout, QLabel, QCheckBox
import random

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.widget = QWidget()
        self.setCentralWidget(self.widget)
        self.main_layout = QVBoxLayout(self.widget)
        
        
        self.setWindowTitle("学号随机生成器")
        
        self.chose_num = set()  # 已经选中过的数字
        
        self.checkbox = QCheckBox("是否重复抽取")
        self.checkbox.setChecked(True)
        self.button_clear = QPushButton("清空选过的学生名单")
        self.button_clear.clicked.connect(self.clearButtonWasClicked)
        layout_0 = QHBoxLayout()
        layout_0.addWidget(self.checkbox)
        layout_0.addWidget(self.button_clear)
        self.main_layout.addLayout(layout_0)
        
        
        self.min_num_label = QLabel("最小的学号")
        self.min_num = QLineEdit()
        self.min_num.setText("1")
        layout_1 = QHBoxLayout()
        layout_1.addWidget(self.min_num_label)
        layout_1.addWidget(self.min_num)
        self.main_layout.addLayout(layout_1)
        
        self.max_num_label = QLabel("最大的学号")
        self.max_num = QLineEdit()
        self.max_num.setText("40")
        layout_2 = QHBoxLayout()
        layout_2.addWidget(self.max_num_label)
        layout_2.addWidget(self.max_num)
        self.main_layout.addLayout(layout_2)
        
        self.top_k_label = QLabel("一次抽取几个")
        self.top_k = QLineEdit()
        layout_3 = QHBoxLayout()
        self.top_k.setText("1")
        layout_3.addWidget(self.top_k_label)
        layout_3.addWidget(self.top_k)
        self.main_layout.addLayout(layout_3)
        
        self.button = QPushButton("开始生成")
        self.button.clicked.connect(self.buttonWasClicked)
        layout_4 = QVBoxLayout()
        layout_4.addWidget(self.button)
        self.main_layout.addLayout(layout_4)
        
        self.show()
    
    def clearButtonWasClicked(self):
        self.chose_num = set()
        QMessageBox.information(self, "Succeed", "已清空选过的学生名单")
    
    def buttonWasClicked(self):
        min_num = int(self.min_num.text())
        max_num = int(self.max_num.text())
        top_k = int(self.top_k.text())
        if min_num >= max_num:
            QMessageBox.information(self, "Error", "错误，要求:最小学号不大于最大学号")
            return

        if top_k > max_num-min_num:
            QMessageBox.information(self, "Error", "错误, 要求:要抽取的学生数量小于学生总数")
            return
        
        if self.checkbox.isChecked():
            # 保证剩余可选的数字是大于topk的
            length = max_num - min_num + 1  #总数量
            length = length - len(self.chose_num)
            if length < top_k:
                QMessageBox.information(self, "Error", "错误，要求:剩余可抽取的学生小于抽取的学生数量, 请清空选过的学生名单")
                return
        
            range_ = list(range(min_num, max_num+1))
            for item in self.chose_num:
                range_.remove(item)
            
        else:
            range_ = list(range(min_num, max_num+1))
            
        random_list = random.sample(range_, top_k)
        message = ""
        for item in random_list:
            message += str(item) + "\n"
            self.chose_num.add(item)
        message = message[:-1]
        QMessageBox.information(self, "succeed", message)
    


app = QApplication([])
window = MainWindow()

app.exec()
