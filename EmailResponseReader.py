#This file reads new emails and looks for "Ack" in them to tell the main project to stop sending alerts for an hour
import imaplib
import email
import TxtFileReader

#Declaring the 'AckChecker' variable outside the function so it can be used outside the function in the other file
AckChecker = None

def CheckEmailforAck():

    #credentials
    username = TxtFileReader.SenderEmail
    password = TxtFileReader.gmailPass

    gmail_host= 'imap.gmail.com' # https://www.systoolsgroup.com/imap/ for different mailboxes (Outlook, Yahoo, etc)
    mail = imaplib.IMAP4_SSL(gmail_host) #set connection
    mail.login(username, password) #login to the mailbox
    mail.select("INBOX") #selects inbox

    global AckChecker  # Creates a global variable that I can use to denote if user acknowledges or not

    #Searches the mailbox for new unread emails
    _, selected_mails = mail.search(None, 'UNSEEN')

    for num in selected_mails[0].split():
        _, data = mail.fetch(num , '(RFC822)')
        _, bytes_data = data[0]

        #convert the byte data to the variable 'message'
        email_message = email.message_from_bytes(bytes_data)
        for part in email_message.walk():
            if part.get_content_type()=="text/plain" or part.get_content_type()=="text/html":
                message = part.get_payload(decode=True)
                #print(message.decode())
                break

        # Searches the email for the word or word starting with "Ack" for "Acknowledge"
        if "Ack" or "ack" in message.decode():
            AckChecker = 1
        else:
            AckChecker = 0



"""
Resource: https://www.techgeekbuzz.com/how-to-read-emails-in-python/
          https://stackoverflow.com/questions/44802930/use-variables-outside-of-function
 """

