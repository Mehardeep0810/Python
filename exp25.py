from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QVBoxLayout
app = QApplication([])
Window = QWidget()
layout = QVBoxLayout()
layout.addWidget(QPushButton('Top'))
layout.addWidget(QPushButton('Bottom'))
Window.setLayout(layout)
Window.show()
app.exec_()
