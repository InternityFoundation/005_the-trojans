#!/usr/bin/python36
import cgi
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

print("content-type:text/html")
print()

m=''' 
<form method="get" >
<center>
<table border="1" style="font-size:20px;">
<tr>
<th>speed(km/hr)</th>
<th>distance(meter)</th>
<th>brake efficiency</th>
</tr>
<tr>
<th><input type=text name="speed" \></th>
<th><input type=text name="dis" \></th>
<th><input type=text name="brake" \></th>
</tr>
<tr>
<th colspan="3"><input type=submit name="submit" \></th>
</tr>
</table>
</center>
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
	
	print("normal-you are driving safely")
	msg="normal-you are driving safely"	
elif pred<3:
	
	print("warning-getting too close, please maintain distance")
	msg="warning-getting too close, please maintain distance"
else:
	msg="alert-may meet an incident/accident"
	print("alert-may meet an incident/accident")

from twilio.rest import Client
account_sid='AC93af9a46fdee6d4f5763166d555dff09'
auth_token='d28688d21486af8fef56cdf15549f572'
client=Client(account_sid,auth_token)

message=client.messages.create(from_='whatsapp:+1415238886',body=msg,to='whatsapp:+917268095504')




