import matplotlib.pyplot as plt
import pfplot as pf

def set_labels(x_label, y_label):
    pf.x_label = x_label
    pf.y_label = y_label
    
def set_legend_loc(loc):
    pf.legend_location = loc
    
def set_colors():
    pass

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
        linestyles = pf.linestyles_seq[:l]
    if markers is None:
        markers = pf.markers_seq[:l]
        
    for i in range(m):
        plot(x, arr2d[:, i], label=labels[i], color=colors[i], linestyle=linestyles[i], marker=markers[i])
    
def plot_error():
    pass
    
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

        plt.plot(pf.x.pop(), pf.y.pop(), label=pf.labels.pop(), color=color, linestyle=linestyle, marker=marker, markersize=pf.marker_size, linewidth=pf.line_width)
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