import datetime
import IP_MonitoringAlerts



def logs():
    import IP_MonitoringAlerts
    now = datetime.datetime.now() #Gets current time and assigns it to 'now' variable
    formattime = now.strftime('%Y-%m-%d %H:%M:%S')  # Formats the time display to be readable

    f = open("Log_for_Alerts.txt","a")

    f.write(formattime + ": " + IP_MonitoringAlerts.ip + " is down \n \n")
    f.close()


def logalert_ack():
    now = datetime.datetime.now() #Gets current time and assigns it to 'now' variable
    formattime = now.strftime('%Y-%m-%d %H:%M:%S')  # Formats the time display to be readable

    f = open("Log_for_Alerts.txt","a")

    f.write(formattime + ": " + IP_MonitoringAlerts.ip + " down alert has not been acknowledged by user. Pausing alerts for 60 minutes \n \n")
    f.close()

def logalert_no_ack():
    now = datetime.datetime.now() #Gets current time and assigns it to 'now' variable
    formattime = now.strftime('%Y-%m-%d %H:%M:%S')  # Formats the time display to be readable

    f = open("Log_for_Alerts.txt","a")

    f.write(formattime + ": " + IP_MonitoringAlerts.ip + " down alert has been not been acknowledged. Sending another alert in 60 seconds \n \n")
    f.close()





