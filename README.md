# IP-Monitoring-Alerts-Email-SMS-Telegram
This project monitors a given list of IP addresses/domain names by pinging and sends an alert via Email/SMS/Telegram if any of them become unresponsive. Users can reply to alerts with an "Ack" to pause alerts for a desired amount of time before the program resumes. (Functioning on Python 3.10)

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



**NOTE**: If you do not want to use Gmail, you will have to change the SMTP server in the SendEmailAlert.py module. You can change the smtp server on line 66.

![image](https://user-images.githubusercontent.com/43974559/166486334-3c0d96fe-81aa-4a22-8112-096d71b54ba5.png)

Simply change "smtp.gmail.com" to your email's SMTP server (i.e. Outlook is "smtp-mail.outlook.com" , Yahoo is "smtp.mail.yahoo.com", etc...)

You can just google your smtp server and change the username and password in the ProjectInfo.json accordingly and it should work.

<br />

### <ins>How to use this program </ins>

There are two files in this folder that need to be filled in: **ProjectInfo.json** and **ip_list.txt**.  

**ProjectInfo.json** will need:
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


![image](https://user-images.githubusercontent.com/43974559/166006930-44aede56-0cc0-4185-8055-83cacf58632b.png)

<br />

The **ip_list.txt** will take in the IP Address/Domain names 
(i.e google.com, exclude the www.) that you would like to monitor in a vertical list. 


![image](https://user-images.githubusercontent.com/43974559/166487154-cebd6cff-88ab-4ce8-8194-976cb111db51.png)

<br />

And that's it! Once you have your info filled and saved in the json and txt file, run the **IP_MonitoringAlerts.py** or **IP_MonitoringAlerts(NoTelegram).py** and voila!

<br />

### <ins>Result </ins>

Telegram bot Alert and acknowledgment:

![image](https://user-images.githubusercontent.com/43974559/166484531-18d18283-2b03-47c8-9ae4-a93960ca55a9.png)


Alert and Acknowledgment Email: 

![image](https://user-images.githubusercontent.com/43974559/166484815-e957358d-b352-44e5-afa2-0ce2be79fb3b.png)

![image](https://user-images.githubusercontent.com/43974559/166241867-35c97ec2-d0d6-4df8-84bd-005585847f26.png)



SMS Alert and Acknowledgment:

![image](https://user-images.githubusercontent.com/43974559/166485016-3c166b2b-78bc-4f39-9c75-81edf5c4b9ca.png)




<br />

### <ins>How it works </ins>

The main module is **IP_MonitoringAlerts.py** and this is where all the other modules are brought together to make this thing work. We'll start with going through this file first.

<br />

The **os** module is a built in Python module that is imported into this file and is used to perform the ping command and it is set to run in an infinite loop so it is constantly pinging the IP/domain given (there are sleep timers later on that you can utilize to manage how often it pings, how long it will wait for a user's acknowledgement before sending another alert, and how long it will pause alerts once receving an acknowledgement). 
The other modules (besides time which is another built in module for pausing the program) are the other files in this project used for various functions:  	

- **TelegramBotAlert** (Sends and reads messages in Telegram)
- **SendEmailAlert** (Sends alert and acknowledgement emails)
- **EmailResponseReader** (Reads responses from user)
- **LoggingAlerts** (Logs events to a file)

There is also a **JSONFileReader** module which reads the values in the JSON document and assigns them to useable variables. 

![image](https://user-images.githubusercontent.com/43974559/166485357-ff713a66-e835-496c-8ac3-b6b5de969efa.png)

<br />

There are two responses that it looks for before sending an alert, if the ping responds with "Destination host unreachable" or "Request timed out." 
The **TelegramBotAlert.bot.sendMessage** sends an Alert message along with the faulted IP. The message it sends can be edited here as well as the **SendEmailAlert**. There is also a **LoggingAlerts** module with a function **logs()** which records the time and date of when the alert was triggered to the **Log_for_Alerts.txt** file. The **time.sleep(60)** has the program wait for the user to send an acknowledgement for 60 seconds before checking for a response. This timer can be easily changed. 


![image](https://user-images.githubusercontent.com/43974559/166485558-eb5afdcd-a1ce-4d01-bc68-db40e450f694.png)

![image](https://user-images.githubusercontent.com/43974559/166485816-0fc96c24-7b45-44a9-a9f6-69613c1a6c2f.png)



<br />

There **EmailResponseReader** module runs the function **CheckEmailforAck()**. This module looks for a response from the user by email/SMS for the word "Ack" or "ack". If it does, it sends an email response, Telegram response, logs the alert has been acknowledged, and pauses the program from running for 60 minutes before resuming. (This time can also be easily changed)

![image](https://user-images.githubusercontent.com/43974559/166485662-99ac2bc7-16a2-4f48-902a-4f162476eb80.png)


<br />

The **TelegramBotAlert** module is run and checks if the user responded with an "Ack" or "ack" via Telegram. If it did, it will send a Telegram response, email response, and log this event. This also has a sleep timer of 60 seconds. 

![image](https://user-images.githubusercontent.com/43974559/166249766-6a59920f-7817-4850-add4-6da23768a778.png)


Lastly, if ping is not down, it waits a desired amount of time before sending another ping

![image](https://user-images.githubusercontent.com/43974559/166485931-9f55686c-ce1d-40d6-8ac6-e7f503b527e5.png)









