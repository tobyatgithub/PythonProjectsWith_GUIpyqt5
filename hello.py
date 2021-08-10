import sys

from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtWidgets import QGridLayout, QPushButton

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Hello App")
window.setGeometry(100, 100, 280, 80)
window.move(60, 15)

layout = QGridLayout()
helloMsg = QLabel("<h1>Hello World!</h1>")
layout.addWidget(helloMsg, 0, 1)
# helloMsg.move(60, 15)
layout.addWidget(QPushButton("Left"), 1, 0)
layout.addWidget(QPushButton("Center"), 1, 1)
layout.addWidget(QPushButton("Right"), 1, 2)

window.setLayout(layout)

window.show()
sys.exit(app.exec_())

