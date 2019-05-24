import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from login import user, password

fromaddr = "from@gmail.com"
toaddr = "to@gmail.com"

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Email about snakes"
body = "Snakes are slithery"
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(user, password)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
