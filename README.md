# IP-Monitoring-Alerts-Email-SMS-Telegram
This project monitors a given list of IP addresses/domain names by pinging and sends an alert via Email/SMS/Telegram if any of them become unresponsive. Users can reply to alerts with an "Ack" to pause alerts for a desired amount of time before the program resumes. 

<br />

### <ins>What you will need</ins>

- (Optional) Telegram bot token, chat ID, Telegram python package (if you would also like to have Telegram notifications)	
 	
	
	- How to get Telegram bot token: https://www.stenge.info/post/telegram-message-with-python
	
	- How to get Chat ID: https://www.alphr.com/find-chat-id-telegram/
	
	- You will also need to install the Python Package for Telepot through admin command line by running "pip install telepot"


- Your SMS Carrier email (You can google your Email to SMS for your specific carrier)
	- The format will be country code then 10 digit number @yourcarrierEmail2SMS.com
		- i.e. +12345678912@yourcarrierEmail2SMS.com


- A gmail account to send emails from with 2-Step Verification turned on and with an App Password
	- To create an app passsword, follow the steps here https://support.google.com/accounts/answer/185833?hl=en
		- This is the password you will use for Gmail Password 


<br />

### <ins>How to use this program </ins>

There are two .txt files in this folder that need to be fillked in: **ProjectInfo.txt** and **ip_list.txt**.  

**ProjectInfo.txt** will need:
- (Optional) Telegram bot token (Leave blank if you do not want Telegram and run the IP_MonitoringAlerts(NoTelegram).py file)
- (Optional) Telegram Chat ID (Leave blank if you do not want Telegram and run the IP_MonitoringAlerts(NoTelegram).py file)
- Gmail password
- Subject for Email
- Sender Email
- Receiver Email
- SMS Email (also used for additional emails you'd like alerts to go to). 
- Alert SMS Text
- Alert Email HTML Body
- Ack SMS Text (This is the response text that is sent to user's acknowledgement of the alert)
- Ack Email HTML Body (This is the response email to user's acknowledgement of the alert)

The **ip_list.txt** will take in the IP Address/Domain names 
(i.e google.com, exclude the www.) that you would like to monitor in a vertical list. 

<br />


### <ins>How it works </ins>

The **subprocess** module is used to perform the ping command and it is set to run in an infinite loop so it is constantly pinging the IP/domain given (there are sleep timers later on that you can utilize to manage how often it pings, how long it will wait for a user's acknowledgement before sending another alert, and how long it will pause alerts once receving an acknowledgement). 

![image](https://user-images.githubusercontent.com/43974559/165816529-4c17f255-7a05-4e10-a7ea-4c6d7140def8.png)


<br />

There are two responses that it looks for before sending an alert, if the ping responds with "Destination host unreachable" or "Request timed out." 
The **TelegramBotAlert.bot.sendMessage** sends an Alert message along with the faulted IP. The message it sends can be edited here as well as the **SendEmailAlert**. There is also a **LoggingAlerts** module with a function **logs()** which records the time and date of when the alert was triggered to the **Log_for_Alerts.txt** file. The **time.sleep(60)** has the program wait for the user to send an acknowledgement for 60 seconds before checking for a response. This timer can be easily changed. 


![image](https://user-images.githubusercontent.com/43974559/165821287-fd881cf9-a75a-40d9-9b75-510029727de1.png)


<br />

There **EmailResponseReader** module runs the function **CheckEmailforAck()**. This module looks for a response from the user by email/SMS for the word "Ack" or "ack". If it does, it sends an email response, Telegram response, logs the alert has been acknowledged, and pauses the program from running for 60 minutes before resuming. (This time can also be easily changed)

![image](https://user-images.githubusercontent.com/43974559/165821391-268a65fe-16ee-4232-8a2d-20f5b3c6f343.png)


<br />

The **TelegramBotAlert** module is run and checks if the user responded with an "Ack" or "ack" via Telegram. If it did, it will send a Telegram response, email response, and log this event. This also has a sleep timer of 60 seconds. 

![image](https://user-images.githubusercontent.com/43974559/165821794-ee41f9a6-a1fc-4412-82a9-9dee8f590399.png)











