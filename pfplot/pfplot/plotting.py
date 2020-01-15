import numpy as np
import matplotlib.pyplot as plt
import pfplot as pf

def reset():
    pf.plot_ins = []
    pf.x = []
    pf.y = []
    pf.labels = []
    pf.colors = []
    pf.linestyles = []
    pf.markers = []    
    pf.__init__('whatever')


def set_labels(x_label, y_label):
    pf.x_label = x_label
    pf.y_label = y_label
    
def set_legend_loc(loc):
    pf.legend_location = loc
    
def set_data_range(data_min, data_max):
    pf.data_min = data_min
    pf.data_max = data_max
    
def set_colors():
    pass
    
def gen_x(mode='step', sample_interval=3):
    x = np.arange(pf.data_min, pf.data_max+1)
    if mode == 'step':
        return x
    if mode == 'min':
        return x*sample_interval
    if mode == 'hour':
        return x * 60 / sample_interval
    
def plot(x, y, label, color=None, linestyle=None, marker=None):
    pf.plot_ins.append('plot')
    pf.x.append(x)
    pf.y.append(y)
    pf.labels.append(label)
    pf.colors.append(color)
    pf.linestyles.append(linestyle)
    pf.markers.append(marker)
    
def plot_array(x, arr2d, labels, colors=None, linestyles=None, markers=None):
    l, m = arr2d.shape[0], arr2d.shape[1]
    if colors is None:
        colors = pf.colors_seq[:l]
    if linestyles is None:
        linestyles = pf.line_styles_seq[:l]
    if markers is None:
        markers = pf.markers_seq[:l]
        
    for i in range(m):
        plot(x, arr2d[:, i], label=labels[i], color=colors[i], linestyle=linestyles[i], marker=markers[i])
    
def plot_error(x, y, yerr, label, color=None, linestyle=None, marker=None):
    pf.plot_ins.append('plot_err')
    pf.x.append(x)
    pf.y.append(y)
    pf.yerr.append(yerr)
    pf.labels.append(label)
    pf.colors.append(color)
    pf.linestyles.append(linestyle)
    pf.markers.append(marker)
    
def plot_error_array(x, arr2d, err_arr2d, labels, colors=None, linestyles=None, markers=None, errorevery=1):
    l, m = arr2d.shape[0], arr2d.shape[1]
    if colors is None:
        colors = pf.colors_seq[:l]
    if linestyles is None:
        linestyles = pf.line_styles_seq[:l]
    if markers is None:
        markers = pf.markers_seq[:l]
        
    pf.errorevery = errorevery
        
    for i in range(m):
        plot_error(x, arr2d[:, i], yerr=err_arr2d[:, i], label=labels[i], color=colors[i], linestyle=linestyles[i], marker=markers[i])
    
def show_states():
    print('States:')
    print('pfplot.x: {}'.format(pf.x))
    print('pfplot.x_: {}'.format(pf.x_))
    
def exec_plot(plt):
    if pf.plot_ins[-1] == 'plot':
        color = pf.colors.pop()
        if color is None:
            color = pf.colors_seq.pop()

        linestyle = pf.linestyles.pop()
        if linestyle is None:
            linestyle = pf.line_styles_seq.pop()
            
        marker = pf.markers.pop()
        if marker is None:
            marker = pf.markers_seq.pop()
        
        plt.plot(pf.x.pop()[pf.data_min:pf.data_max+1], pf.y.pop()[pf.data_min:pf.data_max+1], 
                label=pf.labels.pop(), color=color, linestyle=linestyle, 
                marker=marker, markersize=pf.marker_size, linewidth=pf.line_width)
        pf.plot_ins.pop()

    
    elif pf.plot_ins[-1] == 'plot_err':
        color = pf.colors.pop()
        if color is None:
            color = pf.colors_seq.pop()

        linestyle = pf.linestyles.pop()
        if linestyle is None:
            linestyle = pf.line_styles_seq.pop()
            
        marker = pf.markers.pop()
        if marker is None:
            marker = pf.markers_seq.pop()
        
        plt.errorbar(pf.x.pop(), pf.y.pop()[pf.data_min:pf.data_max+1], yerr=pf.yerr.pop()[pf.data_min:pf.data_max+1], label=pf.labels.pop(), 
                    color=color, linestyle=linestyle, marker=marker, markersize=pf.marker_size, linewidth=pf.line_width,
                    capsize=pf.capsize, elinewidth=pf.error_bar_line_width, errorevery=pf.errorevery)
        pf.plot_ins.pop()
        
    
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
        
    pf.plt_tmp = plt
    return plt
    
def show():
    if pf.plt_tmp is None:
        construct_figure()
    pf.plt_tmp.show()
    
def savefig(name):
    if pf.plt_tmp is None:
        construct_figure()
    pf.plt_tmp.savefig(name)
    print('Figure saved:\n{}'.format(name))