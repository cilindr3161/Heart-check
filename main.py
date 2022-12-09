from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)
 
from instr import *
from second_win import *
     
class MainWin(QWidget):
   def __init__(self):
       ''' окно, в котором располагается приветствие '''
       super().__init__()
