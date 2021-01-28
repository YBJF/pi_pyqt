from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import os

def my_click():
	os.system("xdg-open ~/2.mp4")

if __name__=='__main__':
	app=QApplication(sys.argv)
	window=QWidget()
	window.setWindowTitle("test")
	screen=QDesktopWidget().screenGeometry()
	window.resize(screen.width(),screen.height())
	

	#font
	label1=QLabel("智能垃圾桶")
	label1.resize(screen.width(),screen.height())	
	label1.setAlignment(Qt.AlignHCenter)
	label1.setStyleSheet("color:blue")
	font=QFont()
	font.setPixelSize(40)
	label1.setFont(font)
	label1.setParent(window)

	label2=QLabel("序号 种类     名称       数量 状态 满载")	
	label2.move(30,60)
	label2.setStyleSheet("color:red")
	font2=QFont()
	font2.setPixelSize(20)
	label2.setFont(font2)
	label2.setParent(window)

	#button
	btn1=QPushButton("视频")
	btn1.setGeometry(screen.width()-600,screen.height()-100,100,50)
	btn1.setParent(window)

	btn2=QPushButton("分类")
	btn2.setGeometry(screen.width()-400,screen.height()-100,100,50)
	btn2.setParent(window)

	btn3=QPushButton("满载")
	btn3.setGeometry(screen.width()-200,screen.height()-100,100,50)
	btn3.setParent(window)

	window.show()

	btn1.clicked.connect(my_click)
    
	sys.exit(app.exec())
