import smtplib,requests,bs4
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
while(1):
    try:
        r= requests.get('https://codeforces.com/')
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("gmail_id", "password")
        msg= MIMEMultipart("alternative")
        msg["Subject"]="Codeforces is working now."
        msg["From"]="sender_gmail_id"
        msg["To"]="receiver_gmail_id"
        text="Codeforces is working now."
        msg.attach(MIMEText(text,"plain"))
        html="<h2>Codeforces is working now.</h2><br/><a href='https://codeforces.com/'>Click here to visit.</a>"
        msg.attach(MIMEText(html, "html"))
        s.sendmail("sender_gmail_id","receiver_gmail_id",msg.as_string())
        s.quit()
        print('sent')
        break
    except:
        print('site is down yet...')
        print('sleeping...')
        time.sleep(60)
        print('Trying again')
        continue
    
