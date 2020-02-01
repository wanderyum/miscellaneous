_version = 0.12

def ver():
    return _version

################
# 默认作图设置 #
################

figsize = (9, 6)
dpi = 150

x_label = 'x label'
y_label = 'y label'

# 字体相关
label_font_size     = 18
tick_font_size      = 14
legend_font_size    = 16


# 作图相关
line_width  = 1.5     
error_bar_line_width = 1
marker_size = 7
x_shifting  = 0
capsize     = 3
colors_seq  = ['C0', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9']

# 可选列表: https://matplotlib.org/api/markers_api.html#module-matplotlib.markers
markers_seq = ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o']    

# 可选: [‘solid’ | ‘dashed’, ‘dashdot’, ‘dotted’ | (offset, on-off-dash-seq) | '-' | '--' | '-.' | ':' | 'None' | ' ' | '']
line_styles_seq = ['solid', 'solid', 'solid', 'solid', 'solid', 'solid', 'solid', 'solid', 'solid', 'solid']

legend_frameon  = True      # legend是否有边框
legend_location = 'best'    # 可选: upper right/upper lef/lower left/lower right/right/center left...
tight_layout = True

# 作图数据范围
data_min = 0
data_max = 100

x_label = ''
y_label = ''

# 存储作图指令
plot_ins    = []
x           = []
y           = []
yerr        = []
labels      = []
colors      = []
linestyles  = []
markers     = []

plt_tmp = None

from .pfcfg import cfg, save_cfg, show_cfg
from .plotting import gen_x, plot, plot_array, plot_error, plot_error_array, show, savefig
from .plotting import reset, set_labels, set_data_range, set_legend_loc
from .plotting import select, group_select

