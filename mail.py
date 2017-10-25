import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

fromaddr = "saiprasanth2007@gmail.com"
toaddr = "saiprasanth2007@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Contact Details of"

'''
form = cgi.FieldStorage()
first_name = form["first_name"]
last_name = form["last_name"]
emal = form["email"]

body = "Name = "first_name + last_name + "\nemail = " + email
'''
body = "Hello World"

msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "password")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)

server.quit()
