import time #Time module for waiting before sending another error messsage
import os #OS module for pinging
import SendEmailAlert
import EmailResponseReader
import LoggingAlerts
from importlib import reload
reload(LoggingAlerts) #the LoggingAlerts module broke somehow, importlib is used to workaround the issue


while True: #Starts an infinite loop to always be monitoring the selected IP(s)
    with open("ip_list.txt") as file:
        park = file.read()
        park = park.splitlines()
        print(f" {park}  \n")
        # ping for each ip in the file
    for ip in park:
        response = os.popen(f"ping {ip} ").read()

     #Sends an Alert if the result of the ping is "Request Timed Out"
        if "Request timed out." in response:
            print(response)
            print(ip + " down (Request Timed Out)" + '\n')
            SendEmailAlert.send_email("IP:" +ip + " is down (Request Timed Out).\v\vPlease reply with 'Ack' to pause alerts for 60 minutes") #Sends email message
            LoggingAlerts.logs() #Log this event
            time.sleep(60) #Waits for user to reply to initial alert before sending another

            #Checks email for acknowledgement response from user and logs if there is or isn't a reply
            EmailResponseReader.CheckEmailforAck()
            if EmailResponseReader.AckChecker == 1:
                SendEmailAlert.ack_email() #Sends an email reply that ack has been received
                LoggingAlerts.logalert_ack() #Logs alert has been acknowledged
                time.sleep(600) #Pauses loop for 60 minutes after user has acknowledged the alert
            if EmailResponseReader.AckChecker != 1:
                LoggingAlerts.logalert_no_ack() #Logs that alert has NOT been acknowledged
            time.sleep(60) #If error is sent but not acknowledged, wait 60 seconds before sending another message (Or however long you would like)

        #Sends an Alert if the result of the ping is "Destination host unreachable"
        if "Destination host unreachable." in response:
            print(response)
            print(ip + " is down (Destination host unreachable)" + '\n')
            SendEmailAlert.send_email("IP:" + ip + " is down (Destination host unreachable).\v\vPlease reply with 'Ack' to pause alerts for 60 minutes")
            LoggingAlerts.logs()  # Log this event
            time.sleep(60) #Waits for user to reply to initial alert before sending another

            # Checks email for acknowledgement response from user and logs if there is or isn't a reply
            EmailResponseReader.CheckEmailforAck()
            if EmailResponseReader.AckChecker == 1:
                SendEmailAlert.ack_email() #Sends an email reply that ack has been received
                LoggingAlerts.logalert_ack()  # Logs alert has been acknowledged
                time.sleep(600) #Pauses loop for 60 minutes after user has acknowledged the alert

            if EmailResponseReader.AckChecker != 1:
                LoggingAlerts.logalert_no_ack() ###Logs that alert has NOT been acknowledged
            time.sleep(60) #If error iS not acknowledged, wait 60 seconds before sending another message (Or however long you would like)

        else:
            time.sleep(3) #Timer to be used to delay between pings
            print(response, "\n") #prints ping response
            print(ip, " is ONLINE") #prints IP and its status



'''
Resources used: https://js.educative.io/edpresso/how-to-ping-multiple-ip-addresses-using-python-script
                https://stackoverflow.com/questions/32423837/telegram-bot-how-to-get-a-group-chat-id
                https://www.opentechguides.com/how-to/article/python/57/python-ping-subnet.html
                https://pythongeeks.org/send-email-using-python/
                https://www.delftstack.com/howto/python/python-run-another-python-script/
                https://stackoverflow.com/questions/1250103/attributeerror-module-object-has-no-attribute (module import bug fix)
'''

