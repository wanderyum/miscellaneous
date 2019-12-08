import matplotlib.pyplot as plt
import pfplot as pf

def set_labels(x_label, y_label):
    pf.x_label = x_label
    pf.y_label = y_label
    
def set_legend_loc(loc):
    pf.legend_location = loc

def plot(x, y, label):
    pf.plot_ins.append('plot')
    pf.x.append(x)
    pf.y.append(y)
    pf.labels.append(label)
    
def plot_error():
    pass
    
def exec_plot(plt):
    if pf.plot_ins[-1] == 'plot':
        plt.plot(pf.x[-1], pf.y[-1], label=pf.labels[-1])
        pf.plot_ins.pop()
        pf.x.pop()
        pf.y.pop()
        pf.labels.pop()
        
    
def construct_figure():
    fig = plt.figure(figsize=pf.figsize, dpi=pf.dpi)
    
    while pf.plot_ins:
        exec_plot(plt)
        
    plt.xlabel(pf.x_label, fontsize=pf.label_font_size)
    plt.ylabel(pf.y_label, fontsize=pf.label_font_size)
    plt.xticks(fontsize=pf.tick_font_size)
    plt.yticks(fontsize=pf.tick_font_size)
    plt.legend(fontsize=pf.legend_font_size, frameon=pf.legend_frameon, loc=pf.legend_location)
    
    if pf.tight_layout:
        plt.tight_layout()
        
    return plt
    
def show():
    plt0 = construct_figure()
    plt0.show()