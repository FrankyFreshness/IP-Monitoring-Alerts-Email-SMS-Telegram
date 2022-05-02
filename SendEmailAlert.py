import smtplib  # importing the SMTP Server module
from email.mime.multipart import MIMEMultipart #Module for html
from email.mime.text import MIMEText #Module for html
import JSONFileReader #Reads the credentials file



def send_email(message):  # This function is called to send emails, 'Message' is replaced by the error message in the main project

    email_subject = JSONFileReader.SubjectEmail  # Subject of email
    sender_add = JSONFileReader.SenderEmail  # This is the email you are sending from
    receiver_add = JSONFileReader.ReceiverEmail  # Where emails go to, if you want SMS, enter your SMS email
    smsEmail_add = JSONFileReader.SMSEmailAdd  # SMS email
    AlertSMSText = JSONFileReader.AlertSMSText #Alert SMS Text message
    HTMLEmailBody = JSONFileReader.AlertHTMLEmailBody  #Alert Email message in HTML format
    password = JSONFileReader.gmailPass  # Password for the email you're sending from

    # Below is creating the SMTP server object by giving the SMPT server an address and port number
    smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
    smtp_server.ehlo()  # setting the ESMTP protocol
    smtp_server.starttls()  # setting up to TLS connection
    smtp_server.ehlo()  # calling the ehlo() again as encryption happens on calling startttls()
    smtp_server.login(sender_add, password)  # logging into the senders email

    rcpt = smsEmail_add.split(",") + [receiver_add]  # Formats the recipients emails
    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = email_subject
    msg['From'] = sender_add
    msg['To'] = receiver_add
    msg['Cc'] = smsEmail_add

    message.encode('utf-8')

    # Create the body of the message (a plain-text is for SMS and HTML is for email)
    text = AlertSMSText + message
    html = HTMLEmailBody + message


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

    email_subject = JSONFileReader.SubjectEmail #Subject of email
    sender_add = JSONFileReader.SenderEmail  # This is the email you are sending from
    receiver_add = JSONFileReader.ReceiverEmail  # Where emails go to, if you want SMS, enter your SMS email
    smsEmail_add = JSONFileReader.SMSEmailAdd  # SMS email
    AcksmsText = JSONFileReader.AckSMSText #SMS Acknowledgement Text message
    AckHTMLEmailBody = JSONFileReader.AckHTMLEmailBody #Body of the Acknowledgement email in HTML format
    password = JSONFileReader.gmailPass  # Password for the email you're sending from

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
    text = AcksmsText
    html = AckHTMLEmailBody

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


