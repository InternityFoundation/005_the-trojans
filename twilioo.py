#this code will send an message to client's whatsapp
from twilio.rest import Client 
#import twilio
account_sid = 'AC93af9a46fdee6d4f5763166d555dff09' 
auth_token = 'd28688d21486af8fef56cdf15549f572' 
client = Client(account_sid, auth_token) 

msg = "the excel sheet"
#send "join cake-shape" from the whatsapp(your number) on which you're receive the message and change the msg if you want to

message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body=msg,      
                              to='whatsapp:+917268095504' 
                          ) 
 
print(message.sid)
