# importing required libraries
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *
import os
import sys


#pip install PyQtWebEngine


class MainWindow(QMainWindow):

	# constructor
	def __init__(self, *args, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)

		self.browser = QWebEngineView()

		self.browser.setUrl(QUrl("http://google.com"))

		self.browser.urlChanged.connect(self.update_urlbar)

		self.browser.loadFinished.connect(self.update_title)

		self.setCentralWidget(self.browser)

		self.status = QStatusBar()

		self.setStatusBar(self.status)

		navtb = QToolBar("Navigation")

		self.addToolBar(navtb)

		back_btn = QAction("<", self)

		back_btn.setStatusTip("Back to previous page")

		back_btn.triggered.connect(self.browser.back)

		navtb.addAction(back_btn)


		next_btn = QAction(">", self)
		next_btn.setStatusTip("Forward to next page")

		next_btn.triggered.connect(self.browser.forward)
		navtb.addAction(next_btn)

		reload_btn = QAction("Reload", self)
		reload_btn.setStatusTip("Reload page")

		reload_btn.triggered.connect(self.browser.reload)
		navtb.addAction(reload_btn)

		home_btn = QAction("Home", self)
		home_btn.setStatusTip("Go home")
		home_btn.triggered.connect(self.navigate_home)
		navtb.addAction(home_btn)

		navtb.addSeparator()


		self.urlbar = QLineEdit()


		self.urlbar.returnPressed.connect(self.navigate_to_url)


		navtb.addWidget(self.urlbar)

		stop_btn = QAction("Stop", self)
		stop_btn.setStatusTip("Stop loading current page")

		stop_btn.triggered.connect(self.browser.stop)
		navtb.addAction(stop_btn)

		self.show()


	def update_title(self):
		title = self.browser.page().title()
		self.setWindowTitle("% s - GlaD Browser" % title)



	def navigate_home(self):


		self.browser.setUrl(QUrl("http://www.google.com"))

	def navigate_to_url(self):


		q = QUrl(self.urlbar.text())

		if q.scheme() == "":

			q.setScheme("http")


		self.browser.setUrl(q)


	def update_urlbar(self, q):

		self.urlbar.setText(q.toString())


		self.urlbar.setCursorPosition(0)


# creating a pyQt5 application
app = QApplication(sys.argv)

# setting name to the application
app.setApplicationName("GlaD Browser")

# creating a main window object
window = MainWindow()

# loop
app.exec_()

#2e7dbc2ad6ffd4647b7435b5912126f415b365ab4372758a9eed4e82a3f0d63f
