import os
import pfplot as pf
import matplotlib.pyplot as plt

def cfg(cfg_dir=None):
    if cfg_dir:
        pass
    elif os.path.exists('.'):
        pass
    
    fig = plt.figure(figsize=pf.figsize, dpi=pf.dpi)
    return fig