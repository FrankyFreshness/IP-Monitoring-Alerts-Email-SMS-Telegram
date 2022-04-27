import smtplib  # importing the SMTP Server module
from email.mime.multipart import MIMEMultipart #Module for html
from email.mime.text import MIMEText #Module for html
import TxtFileReader #Reads the credentials file



def send_email(message):  # This function is called to send emails, 'Message' is replaced by the error message in the main project


    sender_add = TxtFileReader.SenderEmail  # This is the email you are sending from
    receiver_add = TxtFileReader.ReceiverEmail  # Where email to email goes to
    smsEmail_add = TxtFileReader.SMSEmail #SMS email
    password = TxtFileReader.gmailPass  # Password for the email you're sending from

    # Below is creating the SMTP server object by giving the SMPT server an address and port number
    smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
    smtp_server.ehlo()  # setting the ESMTP protocol
    smtp_server.starttls()  # setting up to TLS connection
    smtp_server.ehlo()  # calling the ehlo() again as encryption happens on calling startttls()
    smtp_server.login(sender_add, password)  # logging into the senders email

    rcpt = smsEmail_add.split(",") + [receiver_add]  # Formats the recipients emails
    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "HQ SERVICE ALERT ⚠️" #<<<<< CHANGE THE SUBJECT LINE HERE
    msg['From'] = sender_add
    msg['To'] = receiver_add
    msg['Cc'] = smsEmail_add

    # Create the body of the message (a plain-text is for SMS and HTML is for email)
    text = "This is an alert for your services \n\n \b IP: " + message
    html = """\
    <html>
      <head></head>
      <body>
        <h1>&#128680; This is an alert for your services &#128680;</h1>
           \v IP: """ + message + """
        </p>
      </body>
    </html>
    """

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)

    smtp_server.sendmail(sender_add, rcpt, msg.as_string()) #Sends the email

    smtp_server.quit()  #Terminates the SMTP server

def ack_email():  # This function is called to reply to user acknowledgement response

    email_subject = TxtFileReader.SubjectEmail #Subject of email
    sender_add = TxtFileReader.SenderEmail  # This is the email you are sending from
    receiver_add = TxtFileReader.ReceiverEmail  # Where emails go to, if you want SMS, enter your SMS email
    smsEmail_add = TxtFileReader.SMSEmail  # SMS email
    password = TxtFileReader.gmailPass  # Password for the email you're sending from

    # Below is creating the SMTP server object by giving the SMPT server an address and port number
    smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
    smtp_server.ehlo()  # setting the ESMTP protocol
    smtp_server.starttls()  # setting up to TLS connection
    smtp_server.ehlo()  # calling the ehlo() again as encryption happens on calling startttls()
    smtp_server.login(sender_add, password)  # logging into the senders email

    rcpt = smsEmail_add.split(",") + [receiver_add] #Formats the recipients emails
    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = email_subject
    msg['From'] = sender_add
    msg['To'] = receiver_add
    msg['Cc'] = smsEmail_add

    # Create the body of the message (a plain-text is for SMS and HTML is for email)
    text = "Your acknowledgement has been received. ✔ \n\n \b Pausing alerts for 60 minutes "
    html = """\
    <html>
      <head></head>
      <body>
        <h1>Your acknowledgement has been received. ✔ </h1>
           \v Pausing alerts for 60 minutes 
        </p>
      </body>
    </html>
    """

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)

    smtp_server.sendmail(sender_add, rcpt, msg.as_string()) #Sends the email

    smtp_server.quit()  #Terminates the SMTP server

ack_email()
