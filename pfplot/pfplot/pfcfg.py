import os
import pfplot as pf
import matplotlib.pyplot as plt

def cfg(cfg_dir=None):
    if cfg_dir:
        print('Config file: {}'.format(cfg_dir))
    elif os.path.exists(os.path.join('.', 'config.json')):
        print('Config file: {}'.format(os.path.join('.', 'config.json')))
    else:
        print('Using default config')
    