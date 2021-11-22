# Going to write the code for the email automation project in this file. 
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# to create html template for the email content
from string import Template

# Html email contents
message = """<html>
    <head></head>
    <body>
        <p style='color:orange;'>This is my first HTML automated email!</p>
        <p>Alessio</p>
    </body>
</html>"""

#connect to the SMTP server
s = smtplib.SMTP(host='smtp.gmail.com', port=587)
s.starttls()
sender_email = 'soleiman.anwary@gmail.com'
sender_email_password = 'enter password'
recipient_email = 'soleiman.anwary@gmail.com'
s.login('sender_email', 'sender_email_password')

# create a message
msg = MIMEMultipart()

# setup the parameters of the message
msg['From'] = 'sender_email'
msg['To'] = 'recipient_email'
msg['Subject'] = 'AUTOMATED EMAIL TEST SOL'
msg.attach(MIMEText(message, 'html'))

# send the message via the server set up earlier.
s.send_message(msg)
del msg
s.quit()
print('e-mail sent ;)')
