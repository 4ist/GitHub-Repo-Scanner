import smtplib
from email.mime.text import MIMEText
from configs import config

def send(recipient, subject, body):
    # Read configs
    senderEmail = config.private["sender"]
    emailPass = config.private["password"]

    if senderEmail == "" or emailPass == "":
        print("Error: sender email or password was blank in private config file (configs/private-config.json)")

    smtpURL = config.public["email"]["SMTPURL"]
    smtpPort = config.public["email"]["SMTPPort"]

    # Build message
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['To'] = recipient

    try:
        # SMTP login 
        print("Logging in to mail server")
        s = smtplib.SMTP_SSL(smtpURL, smtpPort)
        s.ehlo()
        s.login(senderEmail, emailPass)
    except:
        print("Error: unable to login to mail server")
        return
        
    try:
        # Send email
        print("Sending email")
        s.sendmail(senderEmail, [recipient], msg.as_string())
        s.quit()
        print("Email sent successfully")

    except:
        print("Error: unable to send email")
        return

