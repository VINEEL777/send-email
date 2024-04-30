import smtplib
from email.message import EmailMessage
def email_alert(subject,body,to):
    msg=EmailMessage()
    msg.set_content(body)
    msg['subject']=subject
    msg['to']=to
    
    user="emails.vineela@gmail.com"
    msg['from']=user
    password='mxkdzszobwaxokez'

    server=smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(user,password)
    server.send_message(msg)

    server.quit()

if __name__=='__main__':
    email_alert ("Urgent: Payment Due Notification",
   ''' Dear xx

    I hope this message finds you well. We wanted to bring to your attention that there is an outstanding payment due on your account.

    Invoice Number: [Enter Invoice Number]
Amount Due: [Enter Amount Due]
Due Date: [Enter Due Date]

Prompt payment is crucial to maintaining the smooth functioning of our services and ensuring uninterrupted support for your needs.

Please take a moment to review the attached invoice or visit [Payment Portal Link] to settle the outstanding amount at your earliest convenience. Should you have any questions or require assistance, please don't hesitate to reach out to our billing department at [Billing Department Contact Information].

Thank you for your prompt attention to this matter. We appreciate your continued partnership and cooperation.

Warm regards,

[Your Name]
[Your Position]
[Your Contact Information]''', "vineelabelamana2024@gmail.com" )
 
