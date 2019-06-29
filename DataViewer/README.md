# Data Viewer

This is a simple python script that plots and shows the fluorescent curve interactively using tkinter and matplotlib.

### Requirements
- Python3
- tkinter
- numpy
- matplotlib
- pandas

### Usage
- Using Data Viewer as an application.
    1. (Optional)Copy the .csv file to the same folder where the DataViewer.py exists and rename it as data.csv.
    2. Open the terminal at the folder
    3. `python3 DataViewer.py`

- Using Data Viewer as a class.
```python
from dataviewer import dataViewer
viewer = dataViewer()
viewer.load_csv('data.csv')
viewer.mainloop()
```
