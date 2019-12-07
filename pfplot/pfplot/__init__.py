_version = 0.1

def ver():
    return _version

################
# 默认作图设置 #
################

figsize = (12, 9)
dpi = 150

# 字体相关
label_font_size     = 18
tick_font_size      = 14
legend_font_size    = 16


# 作图相关
line_width  = 1.5
x_shifting  = 0
capsize     = 3

legend_frameon  = True      # legend是否有边框
legend_location = 'best'    # 可选: upper right/upper lef/lower left/lower right/right/center left...
tight_layout = True

# 作图数据范围
data_min = 0
data_max = 1000

x_label = ''
y_label = ''

from .pfcfg import cfg
from .plotting import plot, plot_error, set_labels
