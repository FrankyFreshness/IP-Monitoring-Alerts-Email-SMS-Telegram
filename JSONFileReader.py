import json

data = {}
txtfile = 'ProjectInfo.json' #Open the txt file

with open(txtfile, encoding="utf8") as file:
    data = json.load(file) #Assigns loading the file to data


tokenID = data['Telegram bot token']

chatID = data['Telegram Chat ID']

gmailPass = data['Gmail password']

SubjectEmail = data['Subject for Email']

SenderEmail = data['Sender Email']

ReceiverEmail = data['Receiver Email']

SMSEmailAdd = data['SMS Email']

AlertSMSText = data['Alert SMS Text']

AlertHTMLEmailBody = data['Alert Email HTML Body']

AckSMSText = data['Ack SMS Text']

AckHTMLEmailBody = data['Ack Email HTML Body']

file.close()







