import os
import tkinter as tk
from tkinter import filedialog

import numpy as np
import pandas as pd
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 使用TkAgg后端
matplotlib.use('TkAgg')

# 是否使用加强版
if os.path.exists(os.path.join('.', 'enhancement.py')):
    enhancing = True
else:
    enhancing = False

class vcsv(tk.Tk):
    def __init__(self):
        pass
        
        
        
if __name__ == '__main__':
    v = vcsv()