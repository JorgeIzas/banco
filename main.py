#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 06:55:54 2019

@author: jorge
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from untitled import Ui_mainWindow
app = QApplication(sys.argv)
window = QMainWindow()
ui = Ui_mainWindow()
ui.setupUi(window)

window.show()
sys.exit(app.exec_())