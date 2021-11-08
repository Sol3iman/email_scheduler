# Going to write the code for the email automation project in this file. 
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# to create html template for the email content
from string import Template

# if we want include images
import base64

# Html email contents
message = """
          <!DOCTYPE html>
           <html>
            <head>
              <title>Dear  !</title>
            </head>
            <> Lorem Ipsum Dolor </p>
           <footer style="background-color: gray;">
              <p style="text-align: center;">Contact us on : 
                             <a href="mailto:haaply.apps@gmail.com">
                             haaply.apps@gmail.com</a></p>
              </footer>
    </body>
  </html>
"""

#connect to the SMTP server
s = smtplib.SMTP(host='smtp.gmail.com', port=587)
s.starttls()
# sender_email = the email address to be used for send emails
# sender_email_password : more information above
s.login('sender_email', 'sender_email_password')

# create a message
msg = MIMEMultipart()

# setup the parameters of the message
msg['From'] = 'sender_email'
msg['To'] = 'recipient_email'
msg['Subject'] = 'email_subject'
msg.attach(MIMEText(message, 'html'))

# send the message via the server set up earlier.
s.send_message(msg)
del msg
s.quit()
print('e-mail sent ;)')
