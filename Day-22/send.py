import smtplib
sender ="kondurukarthik3@gmail.com"
receiver = "karthikkonduru148@gmail.com"
password ="ccwagjkxniddumzs"
msg=" Hi dear "
server =smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login(sender,password)
server.sendmail(sender,receiver,msg)
server.quit()
print("mail was sent sucessfully")