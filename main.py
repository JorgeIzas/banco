#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 06:55:54 2019

@author: jorge
"""

import sys
import pymysql
import mysql.connector
from PyQt5.QtWidgets import QApplication, QMainWindow
from untitled import Ui_mainWindow

db = pymysql.connect("localhost","root","gameBoy_444","banco")
cursor = db.cursor()

app = QApplication(sys.argv)
window = QMainWindow()
ui = Ui_mainWindow()
ui.setupUi(window)

window.show()
db.close()
sys.exit(app.exec_())