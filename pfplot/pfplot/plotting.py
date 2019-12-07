
import pfplot as pf

def set_labels(x_label, y_label):
    pf.x_label = x_label
    pf.y_label = y_label

def plot(cfg_dir=None):
    pfplot.cfg(cfg_dir=cfg_dir)
    #print(pfplot.capsize)
    
def plot_error():
    pass