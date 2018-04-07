# vgcollect-monthly-expenses

## Description
Easily track and visualize your monthly expenses from your [VGCollect](https://vgcollect.com) data.

![Image of the graph](https://github.com/deuxbot/vgcollect-monthly-expenses/blob/master/img.png)

## Requisites
- Python3
- Matplotlib
### Windows 10
- Download and install [Python3](https://www.python.org/downloads/)
- Install Matplotlib: open the command line and run ```pip install matplotlib```
### Ubuntu 16
- Install Matplotlib: ```python3 -mpip install -U matplotlib```
- Install Tkinter: ```sudo apt-get install python3-tk```

## Usage
Download your collection in CSV format:    
*Go to VGCollect website > Setttings > Export Data > Collection*  
With the CSV file and the python code in the same directory run:  
```python main.py```  
If the CSV file is in other directory run:  
```python main.py pathToCSV```
