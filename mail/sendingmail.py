# import smtplib
# from email.mime.text import MIMEText

# smtp_ssl_host = 'smtp.gmail.com'  # smtp.mail.yahoo.com
# smtp_ssl_port = 465
# username = 'ernavdeepkr@gmail.com'
# password = 'amandeepsingh'
# sender = 'ernavdeepkr@gmail.COM'
# targets = ['navdeep.navu56.COM', 'savitojs@gmail.com']

# msg = MIMEText('Hi, how are you today?')
# msg['Subject'] = 'Hello'
# msg['From'] = sender
# msg['To'] = ', '.join(targets)

# server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
# server.login(username, password)
# server.sendmail(sender, targets, msg.as_string())
# server.quit()

# Python code to illustrate Sending mail 
# to multiple users 
# from your Gmail account 
import smtplib 

# list of email_id to send the mail 
li = ["navdeep.navu56@gmail.com", "savitojs@gmail.com", "er.amandeepsingh21@gmail.com"] 

for i in range(len(li)): 
	s = smtplib.SMTP('smtp.gmail.com', 587) 
	s.starttls() 
	s.login("ernavdeepkr", "amandeepsingh") 
	message = "I m learning python so could u help me to continue further....btw this is my first project "
	s.sendmail("ernavdeepkr", li[i], message)
    s.sendmail()
	s.quit()