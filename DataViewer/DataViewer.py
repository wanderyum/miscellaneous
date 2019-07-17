#!/usr/bin/env python3

import os
import numpy as np
import pandas as pd
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2TkAgg
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import tkinter as tk
from tkinter import filedialog

# 使用TkAgg后端
matplotlib.use('TkAgg')


'''
默认设置。 如果目录中有"dvcfg.json"则设置会被覆盖。
'''
cfg_def = {}
# 窗口控件字体设置
widgetfont = {'label': ('times', 14, 'roman'),
        'button': ('times', 18, 'bold')
        }
 
# legend中所用字体, 支持中文
legendfontdir = r'c:\windows\fonts\simsun.ttc'
# 画布大小
figsize = (6, 4)
# 显示的DPI
dpi = 150

cfg_def['wid_ft'] = widgetfont
cfg_def['leg_ft_dir'] = legendfontdir
cfg_def['figsize'] = figsize
cfg_def['dpi'] = dpi

class dataViewer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.wm_title('Data Viewer')
        self.protocol('WM_DELETE_WINDOW', self._quit)
        self.resizable(width=False, height=False)
        
        self.load_cfg()

        self.btn = {}
        
        self.createCanvas()
        
    def load_cfg(self):
        self.cfg = cfg_def
        for root, dirs, files in os.walk('.'):
            pass
        if 'dvcfg.json' in files:
            import json
            with open('dvcfg.json') as f:
                str_cfg = ''.join(f.readlines())
            cfg = json.loads(str_cfg)
            
            for key in cfg:
                self.cfg[key] = cfg[key]
        self.cfg['leg_ft'] = FontProperties(fname=self.cfg['leg_ft_dir'])
        
    def show_cfg(self):
        for item in self.cfg:
            print('{}:\t{}'.format(item,self.cfg[item]))
        
    def load_data(self, df, title=''):
        self.vars = {}
        self.btn = {}
        self.df = df
        self.labels = self.df.axes[1]
        self.set_color()
        self.tmp = np.asarray(self.df)
        self.length = self.tmp.shape[0]
        self.maximum = np.max(self.tmp)
        self.maximum = (self.maximum // 500 + 1) * 500
        self.minimum = np.min(self.tmp)
        self.minimum = (self.minimum // 500 ) * 500
        self.title = title
        self.createWidget()
        
    def load_csv(self, path, title=''):
        df = pd.read_csv(path)
        self.load_data(df, title)
    
    def set_color(self):
        self.color = {}
        for i in range(len(self.labels)):
            self.color[self.labels[i]] = 'C' + str(i)

    def createCanvas(self):
        fig = plt.figure(figsize=self.cfg['figsize'], dpi=self.cfg['dpi'])
        self.ax = fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(fig, master=self)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.canvas._tkcanvas.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)

        toolbar = NavigationToolbar2TkAgg(self.canvas, self)
        toolbar.update()
        self.rightframe = tk.Frame(master=self)
        self.rightframe.pack(side=tk.RIGHT)

        self.btnpanel = tk.Frame(master=self.rightframe)
        self.btnpanel.pack(side=tk.TOP)
        tk.Button(master=self.btnpanel, font=self.cfg['wid_ft']['button'], text='打开', command=self.openfile).pack(side=tk.LEFT)
        tk.Button(master=self.btnpanel, font=self.cfg['wid_ft']['button'], text='退出', command=self._quit).pack(side=tk.LEFT)
        self.funcpanel = tk.Frame(master=self.rightframe)
        self.funcpanel.pack(side=tk.TOP)
        tk.Button(master=self.funcpanel, font=self.cfg['wid_ft']['button'], text='反选', command=self.reverse).pack(side=tk.LEFT)
        tk.Button(master=self.funcpanel, font=self.cfg['wid_ft']['button'], text='全选', command=self.select_all).pack(side=tk.LEFT)
        
    
    def createWidget(self):
        for key in self.labels:
            self.vars[key] = tk.IntVar()
            btn = tk.Checkbutton(master=self.rightframe, text=key, variable=self.vars[key], width=45, onvalue=1, offvalue=0, command=self.draw)
            self.btn[key] = btn
            btn.select()
            btn.config(font=self.cfg['wid_ft']['label'])
            btn.pack(side=tk.TOP)
        self.draw()

    def draw(self):
        x = np.linspace(0, self.length-1, self.length)
        self.ax.clear()

        for key in self.labels:
            if self.vars[key].get() > 0:
                y = np.asarray(self.df.loc[:,[key]]).reshape(-1)
                self.ax.plot(x, y, label=key, color=self.color[key])
        self.ax.set_ylim([self.minimum, self.maximum])
        self.ax.set_xlim([0,self.length])
        if self.title:
            self.ax.set_title(self.title)
        self.ax.legend(prop=self.cfg['leg_ft'])
        self.canvas.draw()

    def openfile(self):
        filename = filedialog.askopenfilename(title='打开csv文件', filetypes=[('csv文件', '*.csv'), ('All Files', '*')], initialdir = '.')
        
        if filename:
            for key in self.btn:
                print(self.btn[key])
                self.btn[key].destroy()
            self.load_csv(filename)

    def reverse(self):
        for key in self.vars:
            if self.vars[key].get() == 1:
                self.btn[key].deselect()
            else:
                self.btn[key].select()
        self.draw()
        
    def select_all(self):
        for key in self.vars:
            self.btn[key].select()
        self.draw()
            
    def _quit(self):
        self.quit()
        self.destroy()

if __name__ == '__main__':
    viewer = dataViewer()
    viewer.show_cfg()
    '''
    if 'data.csv' in files:
        viewer.load_csv('data.csv',title='TEST Title')
    '''
    viewer.mainloop()
