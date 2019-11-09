#!/usr/bin/python36
import cgi
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

print("content-type:text/html")
print()

m=''' 
<form method="get">
speed<input type=text name="speed" \><br>
distance<input type=text name="dis" \><br>
brake efficiency<input type=text name="brake" \><br>
<input type=submit name="submit" \><br>
</form>
'''

print(m)

w=cgi.FieldStorage()
f=w.getvalue("speed")
j=w.getvalue("dis")
z=w.getvalue("brake")

#f="30"
#j="3"
#z="80"
print(f,j,z)

b = pd.read_csv("horse1.csv")
x= b[['speed','dis','brake']]
y= b.rate
regr=LinearRegression()
regr.fit(x,y)

f=float(f)
j=float(j)
z=float(z)
pred=regr.predict([[f,j,z]])


print(pred)

if pred<2:
	
	print("normal")
	
elif pred<3:
	
	print("warning")
else:
	
	print("alert")



print("_"*30)




