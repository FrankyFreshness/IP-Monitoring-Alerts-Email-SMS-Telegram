# IP-Monitoring-Alerts-Email-SMS-Telegram
This project monitors a given list of IP addresses/domain names by pinging and sends an alert via Email/SMS/Telegram if any of them become unresponsive. Users can reply to alerts with an "Ack" to pause alerts for a desired amount of time before the program resumes. 
### What you will need for this program ###

- (Optional) Telegram bot token, chat ID, Telegram python package (if you would also like to have Telegram notifications)	
 	
	
	- How to get token: https://www.stenge.info/post/telegram-message-with-python
	
	- How to get Chat ID: https://www.alphr.com/find-chat-id-telegram/
	
	- You will also need to install the Python Package for Telepot through admin command line "pip install telepot"


- Your SMS Carrier email (You can google your Email to SMS for your specific carrier)
	- The format will be country code then 10 digit number @yourcarrierEmail2SMS.com
		- i.e. +12345678912@yourcarrierEmail2SMS.com


- A new gmail account with 2-Step Verification turned on and with an App Password
	- To create an app passsword, follow the steps here https://support.google.com/accounts/answer/185833?hl=en
		- This is the password you will use for Gmail Password 


### How to use this program ###

There are two .txt files in this folder that need to be edited, they are
named Credentials and ip_list. 

Credentials will need:
- (Optional) Telegram bot token (Leave blank if you do not want Telegram and run the IP_MonitoringAlerts(NoTelegram).py file)
- (Optional) Telegram Chat ID (Leave blank if you do not want Telegram and run the IP_MonitoringAlerts(NoTelegram).py file)
- Gmail password
- Subject for Email
- Sender Email
- Receiver Email
- SMS Email (also used for additional emails you'd like alerts to go to). 

The ip_list will take in the IP Address/Domain names 
(i.e google.com, exclude the www.) that you would like to monitor in a vertical list. 

In SendEmailAlert.py, you can edit and change the subject line, 'html' variable
for the body of your email, and the 'text' variable for SMS messages. 







