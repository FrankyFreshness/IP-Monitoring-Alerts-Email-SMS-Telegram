import subprocess #Module for running the ping command and inspecting the output for error strings
import time #Time module for waiting before sending another error messsage
import SendEmailAlert
import EmailResponseReader
import LoggingAlerts
from importlib import reload
reload(LoggingAlerts) #the LoggingAlerts module broke somehow, importlib is used to workaround the issue


# Configure subprocess to hide the console window
info = subprocess.STARTUPINFO()
info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
info.wShowWindow = subprocess.SW_HIDE

while True: #Starts an infinite loop to always be monitoring the selected IP(s)

    with open("ip_list.txt") as file:
        park = file.read()
        park = park.splitlines()
        print(f" {park}  \n")
        # ping for each ip in the file
    for ip in park:
        output = subprocess.Popen(['ping', '-n', '1', '-w', '500', ip], stdout=subprocess.PIPE,
                                  startupinfo=info).communicate()[0]

     #Sends a message if the result of the ping is unresponsive
        if "Destination host unreachable" in output.decode('utf-8'):
            print(ip + " is Offline" + '\n')
            SendEmailAlert.send_email("IP:" +ip + " is down.\v\vPlease reply with 'Ack' to pause alerts for 60 minutes") #Sends email message
            LoggingAlerts.logs() #Log this event
            time.sleep(10) #Waits for user to reply to initial alert before sending another

            #Checks email for acknowledgement response from user and logs if there is or isn't a reply
            EmailResponseReader.CheckEmailforAck()
            if EmailResponseReader.AckChecker == 1:
                SendEmailAlert.ack_email() #Sends an email reply that ack has been received
                LoggingAlerts.logalert_ack() #Logs alert has been acknowledged
                time.sleep(600) #Pauses loop for 60 minutes after user has acknowledged the alert
            if EmailResponseReader.AckChecker != 1:
                LoggingAlerts.logalert_no_ack() #Logs that alert has NOT been acknowledged
            time.sleep(10) #If error is sent, wait 60 seconds before sending another message (Or however long you would like)

        elif "Request timed out" in output.decode('utf-8'):
            print(ip + " is Offline" + '\n')
            SendEmailAlert.send_email("IP:" + ip + " is down.\v\vPlease reply with 'Ack' to pause alerts for 60 minutes")
            LoggingAlerts.logs()  # Log this event
            time.sleep(10) #Waits for user to reply to initial alert before sending another

            # Checks email for acknowledgement response from user and logs if there is or isn't a reply
            EmailResponseReader.CheckEmailforAck()
            if EmailResponseReader.AckChecker == 1:
                SendEmailAlert.ack_email() #Sends an email reply that ack has been received
                LoggingAlerts.logalert_ack()  # Logs alert has been acknowledged
                time.sleep(600) #Pauses loop for 60 minutes after user has acknowledged the alert

            if EmailResponseReader.AckChecker != 1:
                LoggingAlerts.logalert_no_ack() ###Logs that alert has NOT been acknowledged
            time.sleep(10) #If error iS not acknowledged, wait 60 seconds before sending another message (Or however long you would like)

        else:
            pass


'''
Resources used: https://js.educative.io/edpresso/how-to-ping-multiple-ip-addresses-using-python-script
                https://stackoverflow.com/questions/32423837/telegram-bot-how-to-get-a-group-chat-id
                https://www.opentechguides.com/how-to/article/python/57/python-ping-subnet.html
                https://pythongeeks.org/send-email-using-python/
                https://www.delftstack.com/howto/python/python-run-another-python-script/
                https://stackoverflow.com/questions/1250103/attributeerror-module-object-has-no-attribute (module import bug fix)
'''

