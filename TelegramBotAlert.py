import telepot
import TxtFileReader
import time
from telepot.loop import MessageLoop


#This is the Telegram bot token, each bot has a unique token
token = TxtFileReader.tokenID

#Chat ID from the Telegram group
receiver_id = TxtFileReader.chatID
bot = telepot.Bot(token)

'''
######NOTE######
#The two lines below can send a text or image. Replace 'Your service is down' for your customized message 
bot.sendMessage(receiver_id, 'Your service is down')

#This line can send a image, just replace the "Screenshot.png" filename
bot.sendPhoto(receiver_id, photo=open('Screenshot.png', 'rb'))
'''


#This reads the response from the user via Telegram and sends an acknowledgement that it was received

TeleAckChecker = None

def botReply(msg):

    global TeleAckChecker

    message = msg['text']

    if message in {"ack","Ack"}: #Checks if 'ack' or 'Ack' was found in the message
        TeleAckChecker = 1

    if message not in {"ack","Ack"}: #Checks if 'ack' or 'Ack' was NOT found in the message
        TeleAckChecker = 0


MessageLoop(bot, botReply).run_as_thread()

# Keep the program running for 5 loops
count = 0

while count < 5: #Runs this in a loop 5 times every 5 seconds checking for a response
    count += 1
    time.sleep(5)


"""Resource: https://telepot.readthedocs.io/en/latest/#receive-messages """