import os
import json
import pfplot as pf
import matplotlib.pyplot as plt

list_functions = [  'ver', 'pfcfg', 'plotting', 
                    'cfg', 'save_cfg', 'gen_x', 'plot', 'plot_array', 'plot_error', 'plot_error_array',
                    'set_labels', 'set_data_range', 'show', 'show_cfg', 'savefig']
list_storage = ['plot_ins', 'x', 'y', 'yerr', 'labels', 'colors', 'linestyles', 'markers', 'plt_tmp']
list_cfg = []
for item in dir(pf):
    if item not in list_functions and item not in list_storage and item[0] != '_':
        list_cfg.append(item)


def cfg(cfg_dir=None):
    if cfg_dir:
        print('Config file: {}'.format(cfg_dir))
        with open(cfg_dir, 'r') as f:
            js = f.readlines()
        js = ''.join(js)
        D = json.loads(js)
        unpacage_cfg(D)
        
    elif os.path.exists(os.path.join('.', 'config.json')):
        print('Config file: {}'.format(os.path.join('.', 'config.json')))
        with open(os.path.join('.', 'config.json'), 'r') as f:
            js = f.readlines()
        js = ''.join(js)
        D = json.loads(js)
        unpacage_cfg(D)
    else:
        print('Using default config')
    
def save_cfg(cfg_dir=None):
    if cfg_dir is None:
        cfg_dir = os.path.join('.', 'config.json')
    D = package_cfg(list_cfg)
    js = json.dumps(D)
    with open(cfg_dir, 'w') as f:
        print(js, file=f)
    
def show_cfg(list_cfg):
    print('Configurations:')
    for item in list_cfg:
        print('pf.{} = {}'.format(item, eval('pf.{}'.format(item))))
        
def package_cfg(list_cfg):
    D = {}
    for item in list_cfg:
        D[item] = eval('pf.{}'.format(item))
    return D
    
def unpacage_cfg(D):
    for key in D:
        if type(D[key]) == type(' '):
            exec('pf.{}=\'{}\''.format(key, D[key]))
        else:
            exec('pf.{}={}'.format(key, D[key]))