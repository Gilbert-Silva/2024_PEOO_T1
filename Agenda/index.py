import streamlit as st 
from retanguloUI import RetanguloUI

#RetanguloUI.main()

import pandas as pd

px = [0, 1, 2, 3]
py = [10, 5, 15, 10]
dic = { "x" : px, "y" : py }
chart_data = pd.DataFrame(dic)
st.line_chart(chart_data, x = "x", y = "y") 

px = [0, 1, 2, 3, 4, 5]
py = []
for x in px:
    py.append(x**2 - 5*x + 6)
dic = { "x" : px, "y" : py }
chart_data = pd.DataFrame(dic)
st.line_chart(chart_data, x = "x", y = "y") 

xmin = 0
xmax = 5
n = 100
d = (xmax - xmin)/n
x = xmin
px = []
py = []
while x < xmax:
    px.append(x)
    py.append(x**2 - 5*x + 6)
    x = x + d
x = xmax
px.append(x)
py.append(x**2 - 5*x + 6) 
dic = { "x" : px, "y" : py }
chart_data = pd.DataFrame(dic)
st.line_chart(chart_data, x = "x", y = "y")    

xmin = 0
xmax = 5
n = 100
d = (xmax - xmin)/n
x = xmin
px = []
py = []
while x < xmax:
    px.append(x)
    py.append(x**3 - 7*x**2 + 14*x -8)
    x = x + d
x = xmax
px.append(x)
py.append(x**3 - 7*x**2 + 14*x -8)
dic = { "x" : px, "y" : py }
chart_data = pd.DataFrame(dic)
st.line_chart(chart_data, x = "x", y = "y")    
